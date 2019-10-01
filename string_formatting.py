from string import Template

aaa = 'Abc'
bbb = 55
ccc = 123.456
ddd = 0b10101100
eee = 0o1234567
fff = 0xFF
ggg = 10
hhh = 5
def jjj(x, y): x * y

# s – strings
# d – decimal integers (base-10)
# f – floating point display
# c – character
# b – binary
# o – octal
# x – hexadecimal with lowercase letters after 9
# X – hexadecimal with uppercase letters after 9
# e – exponent notation

#
# LITERAL STRING INTERPOLATION
#
print('LITERAL STRING INTERPOLATION:')
print(f'{aaa} {bbb} {ccc}')
print(f'{ggg + hhh} {jjj(2, 4)}')
print(f'{aaa:s} {bbb * 4:x} {bbb * 4:X}')
print(f'{aaa:<20s}')
print(f'{aaa:^20s}')
print(f'{aaa:>20s}')
print(f'{aaa:=<20s}')
print(f'{aaa:=^20s}')
print(f'{aaa:=>20s}')
print(f'{aaa.upper()}')
print(f'{aaa.lower()}')
print()

#
# NEW STYLE
#
print('NEW STYLE:')
print('{:s} {:d} {:f} {:b} {:o} {:x} {:X} {:e}'.format(aaa, bbb, ccc, ddd, eee, fff, fff, bbb))
print('{aaa} {bbb}'.format(aaa=aaa, bbb=bbb))
print('{:.2f}'.format(ccc))
print('{:10.2f}'.format(ccc))
print('{:010.2f}'.format(ccc))
print('{:<20s}'.format(aaa))
print('{:^20s}'.format(aaa))
print('{:>20s}'.format(aaa))
print('{:#<20s}'.format(aaa))
print('{:#^20s}'.format(aaa))
print('{:#>20s}'.format(aaa))
print()

#
# OLD STYLE
#
print('OLD STYLE:')
print('%s %d %f' % (aaa, bbb, ccc))
print('%(aaa)s %(bbb)d' % {'aaa': aaa, 'bbb': bbb})
print('%.2f' % ccc)
print('%10.2f' % ccc)
print('%010.2f' % ccc)
print('%10s' % aaa)
print()

#
# TEMPLATES
#
print('TEMPLATES:')
print(Template('$aaa $bbb').substitute(aaa=aaa, bbb=bbb))
print()
