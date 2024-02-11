import pandas as pd

class TextToExcelConverter:
    def __init__(self, txt_file_path, excel_file_path):
        self.txt_file_path = txt_file_path
        self.excel_file_path = excel_file_path

    def read_txt_file(self):
        """Reads lines from a text file and returns a list of lines without newline characters."""
        try:
            with open(self.txt_file_path, 'r') as file:
                lines = file.readlines()
            return [line.strip() for line in lines]
        except FileNotFoundError:
            print(f"Error: The file {self.txt_file_path} was not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading {self.txt_file_path}: {e}")
            return None

    def convert_to_excel(self):
        """Converts the list of lines from the text file into an Excel file."""
        lines = self.read_txt_file()
        if lines is not None:
            try:
                df = pd.DataFrame(lines, columns=['Text'])
                df.to_excel(self.excel_file_path, index=False, engine='openpyxl')
                print("Conversion completed successfully!")
            except Exception as e:
                print(f"An error occurred while writing to {self.excel_file_path}: {e}")
        else:
            print("Conversion failed due to an earlier error.")

# Example usage
if __name__ == "__main__":
    txt_file_path = '/home/ahmad/Desktop/text_prompts.txt'
    excel_file_path = '/home/ahmad/Desktop/excel_prompt_data.xlsx'
    converter = TextToExcelConverter(txt_file_path, excel_file_path)
    converter.convert_to_excel()
