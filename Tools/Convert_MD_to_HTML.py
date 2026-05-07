import os
import markdown
import codecs

css_style = """
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 900px;
        margin: 0 auto;
        padding: 40px;
        background-color: #f4f7f6;
    }
    .container {
        background-color: #ffffff;
        padding: 50px;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    h1, h2, h3 {
        color: #2c3e50;
        margin-top: 32px;
        margin-bottom: 16px;
        font-weight: 600;
    }
    h1 {
        border-bottom: 3px solid #1a73e8;
        padding-bottom: 0.5em;
        text-align: center;
        color: #1a73e8;
    }
    h2 {
        border-bottom: 2px solid #eaecef;
        padding-bottom: 0.3em;
        color: #d35400;
    }
    h3 {
        color: #27ae60;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 30px;
        font-size: 1.05em;
    }
    th, td {
        border: 1px solid #dfe2e5;
        padding: 12px 16px;
        text-align: left;
    }
    th {
        background-color: #f6f8fa;
        font-weight: bold;
        color: #24292e;
    }
    tr:nth-child(even) {
        background-color: #fafbfc;
    }
    tr:hover {
        background-color: #f1f8ff;
    }
    blockquote {
        margin: 0;
        padding: 16px 20px;
        background-color: #f0f4f8;
        border-left: 5px solid #1a73e8;
        border-radius: 4px;
        color: #4a5568;
    }
    hr {
        height: 0.25em;
        padding: 0;
        margin: 40px 0;
        background-color: #e1e4e8;
        border: 0;
    }
    code {
        background-color: #f6f8fa;
        padding: 0.2em 0.4em;
        border-radius: 3px;
        font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
        font-size: 85%;
    }
    li {
        margin-bottom: 8px;
    }
    em {
        color: #7f8c8d;
        font-size: 0.9em;
    }
</style>
"""

def convert_md_to_html():
    # Thư mục gốc dự án (cha của thư mục Tools)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    count = 0
    # Quét toàn bộ các thư mục con
    for current_root, dirs, files in os.walk(root_dir):
        # Bỏ qua thư mục .git và Tools
        if '.git' in current_root or 'Tools' in current_root:
            continue
            
        for file in files:
            if file.endswith('.md'):
                input_path = os.path.join(current_root, file)
                html_file = os.path.splitext(file)[0] + ".html"
                output_path = os.path.join(current_root, html_file)

                print(f"Dang chuyen doi: {file}...")

                try:
                    with codecs.open(input_path, mode="r", encoding="utf-8") as f:
                        text = f.read()

                    # Format lại các khối ghi chú đặc biệt (Github Alert syntax)
                    text = text.replace("> [!NOTE]", "> **[GHI CHÚ QUAN TRỌNG]**<br>")
                    text = text.replace("> [!TIP]", "> **[MẸO HAY]**<br>")

                    # Chuyển Markdown sang HTML
                    html_content = markdown.markdown(text, extensions=['tables'])

                    # Tiêu đề file HTML lấy từ tên file
                    title = file.replace(".md", "").replace("_", " ")

                    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {css_style}
</head>
<body>
    <div class="container">
        {html_content}
    </div>
</body>
</html>
"""

                    with codecs.open(output_path, mode="w", encoding="utf-8") as f:
                        f.write(full_html)
                    
                    count += 1
                except Exception as e:
                    print(f"Loi khi chuyen doi {file}: {e}")

    if count == 0:
        print("Khong tim thay file .md nao trong du an.")
    else:
        print(f"\nDa hoan tat chuyen doi {count} file!")

if __name__ == "__main__":
    convert_md_to_html()
    print("\nNhan Enter de thoat.")
    input()
