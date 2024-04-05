def filter_file(input_filename, keyword, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
    
        keyword = keyword.lower()
    
    # Обираємо потрібні рядки
    filtered_lines = [line for line in lines if keyword in line.lower()]

    # Записуємо результат у новий файл
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.writelines(filtered_lines)

input_filename = "file.txt"
keyword = "rur"
output_filename = "filtered.txt"

# Викликаємо функцію для виконання фільтрації
filter_file(input_filename, keyword, output_filename)

print(f"Результат фільтрації збережено у файлі '{output_filename}'")
