import asyncio


output_map = {
    True: "Yes",
    False: "No",
}


async def calc_string(string: str) -> str:
    stack = []
    for char in string:
        if char == '#':
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


async def main():
    s1, s2 = map(str, input().split())

    s1, s2 = await asyncio.gather(
        calc_string(s1), calc_string(s2),
    )

    print(output_map[s1 == s2])


asyncio.run(main())
