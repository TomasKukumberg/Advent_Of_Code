def get_instructions(path):
    with open(path) as f:
        return f.read().splitlines()
    
def get_new_instructions(instructions):
    new_instructions = []
    for instruction in instructions:
        if instruction == 'noop':
            new_instructions.append(0)
        else:
            new_instructions.append(0)
            new_instructions.append(int(instruction.split()[1]))
    return new_instructions

def draw_pixel(sprite_position, idx):
    if idx in [sprite_position, sprite_position + 1, sprite_position + 2]:
        return '#'
    return '.'

def render_drawing(drawing):
    for i in range(0, len(drawing), 40):
        print(''.join(drawing[i:i+40]))

def main():
    instructions = get_instructions('input.txt')
    new_instructions = get_new_instructions(instructions)
    x_register = 1
    signal_sum = 0
    sprite_position = 0
    drawing = []
    
    for idx, instruction in enumerate(new_instructions):
        drawing.append(draw_pixel(sprite_position, idx % 40))
        if (idx + 1) in (20, 60, 100, 140, 180, 220):
            signal_strength = (idx + 1) * x_register
            signal_sum += signal_strength
        x_register += instruction
        sprite_position = x_register - 1

    print(f'Signal sum: {signal_sum}')
    render_drawing(drawing)

main()