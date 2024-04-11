import os
import glob

# 获取所有的Markdown文件
markdown_files = glob.glob(
    "Documentation/Observation/Documentation/**/*.md",
    recursive=True,
)


def concat_markdown_files(markdown_files, output_file):
    # 创建一个新的Markdown文件
    with open(f"Documentation/Observation/{output_file}", "w") as outfile:
        for md_file in markdown_files:
            # 获取文件名作为标题
            title = os.path.basename(md_file).replace(".md", "")
            # 写入标题
            outfile.write(f"# {title}\n\n")

            with open(md_file, "r") as infile:
                # 将每个文件的内容写入到新的文件中
                outfile.write(infile.read())
                # 在每个文件之间添加一个换行符，以保持原有的格式
                outfile.write("\n\n")


# 将 markdown_files 中所有相同字母开头的文件合并
concat_markdown_files(markdown_files, f"Observation.md")
