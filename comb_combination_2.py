from matplotlib import pyplot as plt

plt.text(0.01, 0.9, '1) 15 участников турнира. Сколько партий?', fontsize=13)
plt.text(0.01, 0.8, 'Если каждый сыграет с каждым, то будут пары.', fontsize=13)
form = r"$С_2^{15} = \frac{15!}{2!(15-2)!} = \frac{15*14*13!}{2!*3!} = \frac{15*14}{2*1} = \frac{15*7}{1} = 105$"
plt.text(0.01, 0.7, form, fontsize=15)
plt.text(0.01, 0.6, '2) У нас даны числа (3, 5, 7, 11, 13, 17)', fontsize=13)
plt.text(0.01, 0.5, 'Сколько дробей и сколько правильных дробей?', fontsize=13)
form = r"$A_6^2 = \frac{6!}{(6-2)!} = \frac{6!}{4!} = \frac{6*5*4!}{4!} = 6*5 = 30 / 2 = 15$"
plt.text(0.01, 0.4, form, fontsize=15)
plt.text(0.01, 0.3, 'Итого 30 дробей и 15 правильных дробей.', fontsize=13)
plt.text(0.01, 0.2, '3) Даны слова (гора), (институт): сколько слов', fontsize=13)
form = r"$N_1 = 4! = 4*3*2*1 = 24_ N_2 = \frac{8!}{2!3!} = 56*60=3360$"
plt.text(0.01, 0.1, form, fontsize=13)
plt.text(0.01, 0.01, 'во втором кол-во букв разделили на кол-во повторов', fontsize=12)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()