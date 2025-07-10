'''
TASK:
We have the string with format: "value=Example.1|897=890|Client1=Alex|Employer=Bank|897=890|date=2023.8.23 13:89|\nvalue=Example.1|Employer=Hospital"
Write a function that parses this string and prints stats in the format:
tag '{tag}' is used '{num}' times per '{num_lines}' lines and has values '{values}'
'''

# Solution:
def string_parser(data: str) -> None:
    tag_counts = {}
    lines = [line for line in data.split('\n') if line]
    
    for line in lines:
        tags = line.split('|')
        for tag in tags:
            if '=' in tag:
                key, value = tag.split('=')
                if key not in tag_counts:
                    tag_counts[key] = {"count": 0, "values": set()}
                tag_counts[key]["count"] += 1
                tag_counts[key]["values"].add(value)

    for key, info in tag_counts.items():
        print(f'tag \'{key}\' is used \'{info["count"]}\' times per \'{len(lines)}\' lines and have values \'{", ".join(info["values"])}\'')

# Example usage
if __name__ == "__main__":
    input_string = "value=Example.1|897=890|Client1=Alex|Employer=Bank|897=890|date=2023.8.23 13:89|\nvalue=Example.1|Employer=Hospital"
    string_parser(input_string)