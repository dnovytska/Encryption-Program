import tkinter as tk


class Interface:
    def __init__(self, master, codification_func, decodification_func):
        self.master = master
        self.codification_func = codification_func
        self.decodification_func = decodification_func
        self.create_widgets()

    def create_widgets(self):
        root = self.master
        root.title("Encryption Program")
        window_width = 756
        window_height = 491
        root.geometry(f"{window_width}x{window_height}")
        root.resizable(False, False)
        root.configure(background="#4a4a4a")
        canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#4A4A4A")
        canvas.pack()

        rectangle_coords = (24, 75, 358, 477)
        canvas.create_rectangle(rectangle_coords, fill="#A7DEB3", outline="#A7DEB3")

        rectangle_coords = (396, 75, 730, 477)
        canvas.create_rectangle(rectangle_coords, fill="#A7DEB3", outline="#A7DEB3")

        rectangle_coords = (138, 10, 619, 61)
        canvas.create_rectangle(rectangle_coords, fill="#55C86E", outline="#55C86E")

        canvas.create_text(380, 35, text="- Encryption Program -", font=("Arial", 24), fill="#FFFFFF")

        rectangle_coords = (30, 81, 351, 117)
        canvas.create_rectangle(rectangle_coords, fill="#4a4a4a", outline="#4a4a4a")

        canvas.create_text(195, 98, text="- Coding Message -", font=("Arial", 20), fill="#FFFFFF")
        canvas.create_text(175, 135, text="Write the message you want to encrypt:", font=("Arial", 13), fill="#4a4a4a")

        rectangle_coords = (403, 81, 724, 117)
        canvas.create_rectangle(rectangle_coords, fill="#4a4a4a", outline="#4a4a4a")

        canvas.create_text(565, 98, text="- Decoding Message -", font=("Arial", 20), fill="#FFFFFF")
        canvas.create_text(550, 135, text="Write the message you want to decrypt:", font=("Arial", 13), fill="#4a4a4a")

        self.input_message = tk.Entry(root, font=("Arial", 12), bd=0)
        self.input_message.place(x=30, y=148, width=321, height=102)

        self.input_decoded_message = tk.Entry(root, font=("Arial", 12), bd=0)
        self.input_decoded_message.place(x=403, y=148, width=321, height=102)

        canvas.create_text(440, 260, text="Your Key:", font=("Arial", 13), fill="#4a4a4a")
        canvas.create_text(65, 260, text="Your Key:", font=("Arial", 13), fill="#4a4a4a")

        self.encryption_key = tk.Entry(root, font=("Arial", 12), bd=0)
        self.encryption_key.place(x=30, y=275, width=321)

        self.decryption_key = tk.Entry(root, font=("Arial", 12), bd=0)
        self.decryption_key.place(x=402, y=275, width=321)

        canvas.create_text(55, 308, text="Result:", font=("Arial", 13), fill="#4a4a4a")
        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="#ffffff", fg="black")
        self.result_label.place(x=30, y=320, width=321, height=102)

        canvas.create_text(425, 308, text="Result:", font=("Arial", 13), fill="#4a4a4a")
        self.result_label_decoded = tk.Label(root, text="", font=("Arial", 12), bg="#ffffff", fg="black")
        self.result_label_decoded.place(x=403, y=320, width=321, height=102)

        submit_button_codification = tk.Button(root, text="CODE", command=self.submit_codification, bg="#4CA660",
                                               fg="white", font=("Arial", 14), bd=0)
        submit_button_codification.place(x=155, y=431)

        submit_button_decodification = tk.Button(root, text="DECODE", command=self.submit_decodification, bg="#4CA660",
                                                 fg="white", font=("Arial", 14), bd=0)
        submit_button_decodification.place(x=530, y=431)

        copy_button_codification = tk.Button(root, text="Copy Result", command=self.copy_result_codification,
                                             bg="#4CA660", fg="white", font=("Arial", 14), bd=0)
        copy_button_codification.place(x=30, y=431)

        copy_button_decodification = tk.Button(root, text="Copy Result", command=self.copy_result_decodification,
                                               bg="#4CA660", fg="white", font=("Arial", 14), bd=0)
        copy_button_decodification.place(x=405, y=431)

    def submit_codification(self):
        coded_message = self.codification_func(self.input_message.get(), self.encryption_key.get())
        self.result_label.config(text=coded_message)

    def submit_decodification(self):
        decoded_message = self.decodification_func(self.input_decoded_message.get(), self.decryption_key.get())
        self.result_label_decoded.config(text=decoded_message)

    def copy_result_codification(self):
        result = self.result_label.cget("text")
        if result:
            self.master.clipboard_clear()
            self.master.clipboard_append(result)

    def copy_result_decodification(self):
        result = self.result_label_decoded.cget("text")
        if result:
            self.master.clipboard_clear()
            self.master.clipboard_append(result)
