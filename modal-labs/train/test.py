def extract_xml_answer(text: str) -> str:
    marker = r"\boxed{"
    start_idx = text.find(marker)
    if start_idx == -1:
        return ""
    # start index after \boxed{
    start_idx += len(marker)

    depth = 1
    i = start_idx
    while i < len(text) and depth > 0:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1

    # If we found a matching closing brace
    if depth == 0:
        return text[start_idx : i - 1].strip()
    else:
        return ""


print(extract_xml_answer("\\boxed{\\dfrac{143}{177147}}"))
