FIO_FORMATTER = {
    "long": lambda s, n, s_n: f"{s} {n}{f' {s_n}' if s_n else ''}",
    "short": lambda s, n, s_n: f"{s[0]}.{n[0]}.{f'{s_n[0]}.' if s_n else ''}",
    "default": lambda s, n, s_n: f"{s} {n[0]}.{f'{s_n[0]}.' if s_n else ''}"
}


def get_format_fio(
        surname: str,
        name: str,
        second_name: str | None = None,
        format_fio: str = "default"
) -> str:
    if format_fio not in FIO_FORMATTER:
        format_fio = "default"

    return FIO_FORMATTER[format_fio](surname, name, second_name)


if __name__ == "__main__":
    print(get_format_fio("Freeman", "Gordon", format_fio="short"))
    