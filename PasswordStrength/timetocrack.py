import string



def timetocrack(password):
    char_set = 0

    if any(c in string.ascii_uppercase for c in password):
        char_set += 26
    if any(c in string.ascii_lowercase for c in password):
        char_set += 26
    if any(c in string.digits for c in password):
        char_set += 10
    if any(c in string.punctuation for c in password):
        char_set += 32



    len_pass = len(password)

    comb = char_set ** len_pass

    speed = pow(10, 9)

    time_taken = (comb/speed)

    # format time properly
    def format_duration(time_taken):
        # Calculate years, months, days, hours, minutes, and seconds
        years = time_taken // (365.25 * 24 * 3600)
        time_taken %= (365.25 * 24 * 3600)
        months = time_taken // (30 * 24 * 3600)
        time_taken %= (30 * 24 * 3600)
        days = time_taken // (24 * 3600)
        time_taken %= (24 * 3600)
        hours = time_taken // 3600
        time_taken %= 3600
        minutes = time_taken // 60
        time_taken %= 60

        # Build the output
        time_parts = []
        if years > 0:
            time_parts.append(f"{years} year{'s' if years > 1 else ''}")
        if months > 0:
            time_parts.append(f"{months} month{'s' if months > 1 else ''}")
        if days > 0:
            time_parts.append(f"{days} day{'s' if days > 1 else ''}")
        if hours > 0:
            time_parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
        if minutes > 0:
            time_parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
        if time_taken > 0:
            time_parts.append(f"{time_taken} second{'s' if time_taken > 1 else ''}")

        return ", ".join(time_parts) if time_parts else "0"

    return format_duration(time_taken)







