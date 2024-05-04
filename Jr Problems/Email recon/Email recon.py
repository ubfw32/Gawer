def r_email():
    n = input('Please insert your name: ')
    m = input('Please insert your email: ')
    u = m[:m.index("@")]
    d = m[m.index("@") + 1:]
    r = d[:d.index('.')]
    print(f"Hey {n.upper()} as {u}, I see your email is registered with {r.upper()}, that's cool")

r_email()