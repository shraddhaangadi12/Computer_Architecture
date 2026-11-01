# Virtual to Physical Address Translation

page_size = 1024

page_table = {
    0: 5,
    1: 2,
    2: None,
    3: 7
}

virtual_addresses = [500, 1500, 2500, 3500]

print("Virtual Address | Page | Offset | Frame | Physical Address")

for va in virtual_addresses:

    page_number = va // page_size
    offset = va % page_size

    if page_number in page_table:
        frame = page_table[page_number]

        if frame is not None:
            physical_address = frame * page_size + offset

            print(va, "|", page_number, "|", offset,
                  "|", frame, "|", physical_address)
        else:
            print(va, "|", page_number, "|", offset,
                  "| Not Present | Page Fault")

    else:
        print(va, "|", page_number, "|", offset,
              "| Not Present | Page Fault")