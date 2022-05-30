import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog, tkinter.messagebox
import os
import shutil
import regex as re
from pathlib import Path

import MeCab
import ipadic
import pykakasi

title = 'RPY-CSV Converter 1.10'

output_dir = [os.path.join('output', 'CSV'), os.path.join('output', 'RPY')]
user_settings_path = 'settings.ini' # オプションの設定履歴
none_path = '...'

lang_code = [['japanese', '_jp'], ['japanese_for_search', '_jp_search'], ]

comma_replacer = re.compile(r',(?=(?:[^"\r\n]*"[^"\r\n]*")*[^"\r\n]*$)', re.MULTILINE | re.DOTALL)

class user_settings: # オプションの設定履歴
    def __init__(self):
        self.defaults = [['rpy_path', none_path], ['csv_path', none_path], ['csv_output_path', output_dir[1]], ['flag_wakatchi', '0']]
        self.current = []

        self.create_txt()
        self.generate_list()

    def create_txt(self): # テキストがなければ作成
        old_lines = []
        new_data = []

        if os.path.isfile(user_settings_path):
            with open(user_settings_path, "r") as f:
                old_lines = f.read().splitlines(False)

        new_data = [line[0] + ':=' + line[1] for idx, line in enumerate(self.defaults)]

        if old_lines:
            for idx, e in enumerate(new_data):
                if idx < len(old_lines):
                    new_data[idx] = old_lines[idx] # 古いファイルにない項目を追加

        if len(new_data) != len(old_lines): # 古いファイルが見つからない OR 追加項目があるなら書き込み
            with open(user_settings_path, "w+") as f:
                f.write('\n'.join(new_data))

    def generate_list(self): # テキストからリストを生成
        with open(user_settings_path, "r") as f:
            lines = f.read()

        for line in lines.splitlines(False):
            separated = re.split(':=', line)
            self.current.append([separated[0], separated[1]])

    def read_by_key(self, key): # リストの値を読み取り

        for data in self.current:
            if data[0] == key:
                if data[1] == 'True': return True
                if data[1] == 'False': return False
                return data[1]

        return ''

    def write_txt(self, *val): # 現在の設定をテキストファイルに書き込み

        if len(val) != len(self.current):
            return

        with open(user_settings_path, "r") as f:
            lines = f.read()

        new_data = []
        for line in lines.splitlines(False):
            separated = re.split(':=', line)

            for idx in range(len(val)):

                if separated[0] == self.current[idx][0]:
                    separated[1] = val[idx]
                    break
            new_data.append(':='.join(map(str, separated)))

        with open(user_settings_path, "w") as f:
            f.write('\n'.join(new_data))

##############################################################################################


class App(tk.Frame): # GUIの設定

    def __init__(self, root):
        super().__init__(root)
        root.title(title)
        root.geometry('600x280')
        root.resizable(width=False, height=False)

        # ユーザー設定の読み込み（インスタンスに読み取り値のリストを作成）
        self.lastused = user_settings()
        
        # 定数の初期化
        self.w_rpy_path = tk.StringVar(value=self.lastused.read_by_key('rpy_path'))
        self.w_csv_path = tk.StringVar(value=self.lastused.read_by_key('csv_path'))
        self.w_csv_output_path = tk.StringVar(value=self.lastused.read_by_key('csv_output_path'))

        self.w_wakatchi = tk.StringVar(value=self.lastused.read_by_key('flag_wakatchi'))

        # Mecabのタグインスタンス
        self.m = MeCab.Tagger(ipadic.MECAB_ARGS)

        # メニューに遷移
        self.main_menu()

    def SetRPYPath(self):
        iDir = os.path.abspath(os.path.dirname(__file__))
        val = tkinter.filedialog.askdirectory(initialdir = iDir)
        val = val.replace('/', os.sep)
        self.w_rpy_path.set(str(val))
        return

    def SetCSVPath(self):
        iDir = os.path.abspath(os.path.dirname(__file__))
        val = tkinter.filedialog.askdirectory(initialdir = iDir)
        val = val.replace('/', os.sep)
        self.w_csv_path.set(str(val))
        return

    def SetCSVOutputPath(self):
        iDir = os.path.abspath(os.path.dirname(__file__))
        val = tkinter.filedialog.askdirectory(initialdir = iDir)
        val = val.replace('/', os.sep)
        self.w_csv_output_path.set(str(val))
        return

    # -----------------------------------------------------------------------------------------------

    def main_menu(self):

        global frame_root

        # ウィジェットの作成
        e_rpy_path = tk.Entry(frame_root, textvariable = self.w_rpy_path, width=72)
        b_rpy_path = tk.Button(frame_root, text = 'パスを指定', command = self.SetRPYPath)
        e_csv_path = tk.Entry(frame_root, textvariable = self.w_csv_path, width=72)
        b_csv_path = tk.Button(frame_root, text = 'パスを指定', command = self.SetCSVPath)
        e_csv_output_path = tk.Entry(frame_root, textvariable = self.w_csv_output_path, width=72)
        b_csv_output_path = tk.Button(frame_root, text = 'パスを指定', command = self.SetCSVOutputPath)

        b_run_rpy2csv = tk.Button(frame_root, text = 'RPY > CSV に変換', padx = 15, command = lambda: self.Run(0))
        b_run_csv2rpy = tk.Button(frame_root, text = 'CSV > RPY に変換', padx = 15, command = lambda: self.Run(1))

        b_wakatchi = tk.Checkbutton(frame_root, text = 'わかち書きを有効', padx = 15, variable = self.w_wakatchi)

        # ウィジェットを配置
        e_rpy_path.grid(column=0, row=1, columnspan=1, padx=5, pady=10, sticky=tk.EW)
        b_rpy_path.grid(column=1, row=1, padx=5, sticky=tk.E)
        b_run_rpy2csv.grid(column=0, row=2, padx=4, pady=10, sticky=tk.S)

        sep = ttk.Separator(frame_root)
        sep.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky=tk.EW)

        e_csv_path.grid(column=0, row=4, columnspan=1, padx=5, pady=10, sticky=tk.EW)
        b_csv_path.grid(column=1, row=4, padx=5, sticky=tk.E)
        e_csv_output_path.grid(column=0, row=5, columnspan=1, padx=5, pady=10, sticky=tk.EW)
        b_csv_output_path.grid(column=1, row=5, padx=5, sticky=tk.E)
        b_run_csv2rpy.grid(column=0, row=6, padx=4, pady=10, sticky=tk.S)

        b_wakatchi.grid(column=0, columnspan=1, row=6, pady=10, sticky=tk.SE)

##############################################################################################


    def Run(self, mode): # CSV の変換処理

        rpy_path = self.w_rpy_path.get()
        csv_path = self.w_csv_path.get()
        csv_output_path = self.w_csv_output_path.get()
        enable_wakatchi = bool(int(self.w_wakatchi.get()))

        if mode == 0 and (not os.path.exists(rpy_path) or rpy_path == none_path):
            tkinter.messagebox.showinfo('RPY が未指定', 'RPY のパスが正しく指定されていません。')
            return
        elif mode == 1 and (not os.path.exists(csv_path) or csv_path == none_path):
            tkinter.messagebox.showinfo('CSV が未指定', 'CSV のパスが正しく指定されていません。')
            return

        # 現在の設定をテキストに書き出し
        self.lastused.write_txt(rpy_path, csv_path, csv_output_path, enable_wakatchi) 

        # -----------------------------------------------------------------------

        # RPY を整形して書き出し

        if mode == 0:
            self.RPY2CSV(rpy_path)
            tkinter.messagebox.showinfo('RPY > CSV', '変換に成功しました！')
        elif mode == 1:
            self.CSV2RPY(csv_path, csv_output_path, enable_wakatchi)
            tkinter.messagebox.showinfo('CSV > RPY', '変換に成功しました！')
        return


    def RPY2CSV(self, input_path):

        raw_data = {}

        for file in os.listdir(input_path):

            file_path = os.path.join(input_path, file)

            if not file_path.endswith('.rpy'): continue

            with open(file_path, 'r', encoding='utf_8_sig') as f:
                lines = f.read()

            lines = re.sub(r'\\"', '”', lines)
            lines = re.sub(r'{', '<', lines)
            lines = re.sub(r'}', '>', lines)

            file_data = []

            for line in lines.splitlines(False):
                if re.search(r'(^$|^[^ ]|^ +$|^ *return *)', line): continue;

                data = re.split(r'\"([^"]+)\"', ''.join(line))
                data = [entry for entry in data if entry != ' ' and not entry.startswith('   ')]
                file_data.append(data)

            raw_data[os.path.splitext(file)[0]] = file_data

        shutil.rmtree(output_dir[0], ignore_errors=True)

        for file in raw_data:
            file_data = raw_data.get(file)

            for entries in file_data:
                # {file: [[label, entry, block, title, writer, dates, lang, data]]}
                output = []
                label_name = entries[0];

                for idx, entry in enumerate(entries):
                    crlf = ''


                    if idx < 5:
                        if idx == 0: key_name = label_name + ':entry';
                        elif idx == 1: key_name = label_name + ':title';
                        elif idx == 2: key_name = label_name + ':writer';
                        elif idx == 3: key_name = label_name + ':date';
                        elif idx == 4: key_name = label_name + ':lang';

                        output.append('{0},"{1}",'.format(key_name, entry))
                        continue
                    elif idx > 5:
                        continue

                    row = 0
                    for content in re.split(r'(.*?(?:\\n)+)', entry):
                        if content == '': continue;

                        key_name = '{0}:content:{1}'.format(label_name, row)
                        output.append('{0},"{1}",""'.format(key_name, content, crlf))

                        row += 1

                output.append('')

                output_path = os.path.join(output_dir[0], file, label_name + '.csv')

                os.makedirs(os.path.split(output_path)[0], exist_ok=True)
                with open(output_path, 'w+', encoding='utf_8_sig') as f:
                    f.write('\n'.join(output))

        return


    def CSV2RPY(self, input_path, output_path, enable_wakatchi):

        file_contents = {}
        wakatchi_contents = {}

        for cur_dir, dirs, files in os.walk(input_path):
            for file in files:

                file_path = os.path.join(cur_dir, file)
                base_file = os.path.split(cur_dir)[1]
                label = re.sub(r'\.[a-z0-9]+$', r'', os.path.split(cur_dir)[1])

                if not file_path.endswith('.csv'): continue

                with open(file_path, 'r', encoding='utf_8_sig') as f:
                    lines = f.read()

                lines = comma_replacer.sub('\t', lines)

                new_data = []
                content = ''

                for idx, line in enumerate(lines.splitlines(False)):
                    entry = line.split('\t')
                    output_line = ''

                    if len(entry) > 2 and entry[2] != '' and entry[2] != '""': output_line = entry[2]; # 翻訳あり
                    elif len(entry) > 1: output_line = entry[1]; # 翻訳なし

                    output_line = output_line.strip('"')
                    output_line = output_line.replace('”', '\\"')
                    output_line = output_line.replace('<', '{')
                    output_line = output_line.replace('>', '}')

                    if output_line != '':
                        if idx > 0 and idx < 5:
                            new_data.append(output_line)
                        elif idx >= 5:
                            content += output_line
                    if idx == 0:
                        block = output_line

                if content and not ' ' in content:
                    content += ' ' # ブロックの取得漏れ防止

                new_data.append(content)
                new_data.insert(0, lang_code[0][0])
                new_data.insert(0, '{0}'.format(block))

                output = ''

                for idx, c in enumerate(new_data):
                    if idx == 0:
                        output += '    ' + 'tl_hateplus_message'
                    output += ' "' + c + '"'

                if not file_contents.get(label):
                    file_contents[label] = output
                else:
                    file_contents[label] = file_contents[label] + '\n' + output

                if not enable_wakatchi:
                    continue

                wakatchi_data = []
                output = ''
                for idx, c in enumerate(new_data):
                    if idx == 0:
                        output += '    ' + 'tl_hateplus_message "' + c + '"'
                    elif idx == 1:
                        output += ' "' + lang_code[1][0] + '"'
                    elif idx >= 2 and idx <= 3:
                        output += ' "' + self.Wakatchi_Format(c, False) + '"'
                    elif idx > 5:
                        output += ' "' + self.Wakatchi_Format(c) + '"'
                    else:
                        output += ' "' + c + '"'

                if not wakatchi_contents.get(label):
                    wakatchi_contents[label] = output
                else:
                    wakatchi_contents[label] = wakatchi_contents[label] + '\n' + output


        for file in file_contents:
            # 通常ファイルを出力
            content = file_contents.get(file)
            output_file = file + lang_code[0][1] + '.dlc2.rpy'

            if not content: continue;
            content = 'label {0}{1}:\n'.format(file, lang_code[0][1]) + content + '\n    return\n'

            dest_path = os.path.join(output_path, output_file)
            os.makedirs(os.path.split(dest_path)[0], exist_ok=True)

            with open(dest_path, 'w+', encoding='utf_8_sig', newline='\n') as f:
                f.write(content)

            # 検索用のわかち書きファイルを出力
            content = wakatchi_contents.get(file)
            output_file = file + lang_code[1][1] + '.dlc2.rpy'

            if not content: continue;
            content = 'label {0}{1}:\n'.format(file, lang_code[1][1]) + content + '\n    return\n'

            dest_path = os.path.join(output_path, output_file)

            with open(dest_path, 'w+', encoding='utf_8_sig', newline='\n') as f:
                f.write(content)


    def Wakatchi_Format(self, content, insert_sp=True):

        self.m.parse("") # デコードエラー防止

        kks = pykakasi.kakasi()
        node = self.m.parseToNode(content)
        hiragana_converted = ''

        Only_Hiragana = re.compile(r'^[\p{Hiragana}]+$')
        while node:
            features = node.feature.split(",") # 形態素をリストに分離
            if len(features) > 8 and features[8] != '' and not Only_Hiragana.search(node.surface):
                c_tmp = kks.convert(features[8])[0].get('hira')
                if c_tmp != '*': hiragana_converted += c_tmp;
            else:
                hiragana_converted += kks.convert(node.surface)[0].get('hira')

            node = node.next

        if insert_sp and not ' ' in hiragana_converted:
            hiragana_converted += ' ' # ブロックの取得漏れ防止

        result = hiragana_converted

        return result

##############################################################################################

if __name__ == "__main__":
    root = tk.Tk()
    frame_root = ttk.Frame(root)
    myapp = App(root)
    frame_root.grid()
    myapp.mainloop()