from Hw7z1 import StackEE


def CheckPair(pairs: dict, item1: str, item2: str) -> bool:
    if pairs[item2] == item1:
        return True
    return False


def CheckBracketsBalance(pairs, instr: str) -> bool:
    if (len(instr) % 2) != 0:
        return False

    stack_obj = StackEE()

    for item in instr:
        if item in "([{":
            stack_obj.push(item)
        else:
            if not CheckPair(pairs, item, stack_obj.pop()):
                return False

    return True


if __name__ == "__main__":

    pairs = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    str = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "}{}",
        "{{[(])]}}",
        "[[{())}]"
    ]

    for current_str in str:
        print(F"{current_str} is balanced = {CheckBracketsBalance(pairs, current_str)}")
