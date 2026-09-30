import tkinter as tk
from tkinter import ttk


def to_newton(value, unit):
    if unit == "kN":
        return value * 1000
    elif unit == "N":
        return value
    elif unit == "kgf":
        return value * 9.80665
    else:
        raise ValueError("지원하지 않는 단위입니다.")


def from_newton(value_in_newton, unit):
    if unit == "kN":
        return value_in_newton / 1000
    elif unit == "N":
        return value_in_newton
    elif unit == "kgf":
        return value_in_newton / 9.80665
    else:
        raise ValueError("지원하지 않는 단위입니다.")


history_list = []


def set_result_text(text):
    result_text.configure(state="normal")
    result_text.delete("1.0", "end")
    result_text.insert("end", text)
    result_text.configure(state="disabled")


def add_history(text):
    history_list.append(text)


def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("변환 기록")
    history_window.geometry("420x260")

    history_text = tk.Text(history_window, wrap="word", font=("맑은 고딕", 11))
    history_text.pack(fill="both", expand=True, padx=10, pady=10)

    if not history_list:
        history_text.insert("end", "기록이 없습니다.")
    else:
        for item in history_list:
            history_text.insert("end", item + "\n")

    history_text.configure(state="disabled")


def convert_force():
    try:
        value = float(entry_value.get())
    except ValueError:
        set_result_text("단위를 변환할 수 없습니다.")
        return

    if value < 0:
        set_result_text("힘은 0 이상의 숫자로 입력하세요.")
        return

    try:
        input_unit = input_unit_var.get()
        output_unit = output_unit_var.get()
        value_in_newton = to_newton(value, input_unit)
        converted_value = from_newton(value_in_newton, output_unit)
    except ValueError:
        set_result_text("단위를 변환할 수 없습니다.")
        return

    result_text_value = f"{value} {input_unit} = {converted_value:.3f} {output_unit}"
    set_result_text(result_text_value)
    add_history(result_text_value)


def refresh_result():
    try:
        value = float(entry_value.get())
    except ValueError:
        set_result_text("단위를 변환할 수 없습니다.")
        return

    if value < 0:
        set_result_text("힘은 0 이상의 숫자로 입력하세요.")
        return

    try:
        input_unit = input_unit_var.get()
        output_unit = output_unit_var.get()
        value_in_newton = to_newton(value, input_unit)
        converted_value = from_newton(value_in_newton, output_unit)
    except ValueError:
        set_result_text("단위를 변환할 수 없습니다.")
        return

    set_result_text(f"{value} {input_unit} = {converted_value:.3f} {output_unit}")


root = tk.Tk()
root.title("힘 단위 변환기")
root.geometry("560x360")
root.resizable(True, True)

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

label_value = ttk.Label(frame, text="값 입력:")
label_value.grid(row=0, column=0, sticky="w", padx=(0, 10), pady=(10, 10))

value_frame = ttk.Frame(frame)
value_frame.grid(row=0, column=1, sticky="ew")

entry_value = ttk.Entry(value_frame, width=18)
entry_value.pack(side="left", fill="x", expand=True)

input_unit_var = tk.StringVar(value="kN")
input_unit_menu = ttk.Combobox(value_frame, textvariable=input_unit_var, values=["kN", "N", "kgf"], state="readonly", width=8)
input_unit_menu.pack(side="left", padx=(10, 0))

input_unit_menu.bind("<<ComboboxSelected>>", lambda event: refresh_result())

label_output_unit = ttk.Label(frame, text="출력 단위:")
label_output_unit.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(0, 10))

output_unit_var = tk.StringVar(value="N")
output_unit_menu = ttk.Combobox(frame, textvariable=output_unit_var, values=["kN", "N", "kgf"], state="readonly", width=8)
output_unit_menu.grid(row=1, column=1, sticky="w", pady=(0, 10))
output_unit_menu.bind("<<ComboboxSelected>>", lambda event: refresh_result())

output_label = ttk.Label(frame, text="출력 결과:")
output_label.grid(row=2, column=0, sticky="nw", padx=(0, 10), pady=(10, 10))

result_text = tk.Text(frame, height=8, width=42, wrap="word", font=("맑은 고딕", 11))
result_text.grid(row=2, column=1, sticky="nsew", pady=(10, 10))
result_text.insert("end", "결과가 여기에 표시됩니다.\n")
result_text.configure(state="disabled")

convert_button = ttk.Button(frame, text="변환", command=convert_force)
convert_button.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(5, 5))

history_button = ttk.Button(frame, text="변환 기록", command=show_history)
history_button.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 0))

frame.columnconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

root.mainloop()