while True:
	countall = 0
	while True:
		import random
		import os
		import time
		if countall > 0:
			print"Do you want start again? Y/N"
			b = raw_input(">")
			if b == "Y" or "y":
				print""
				os.system("cls")
			elif b == "N" or "n":
				os._exit()
			else:
				print"don't enter wrong number!"
				time.sleep(3)
				os.system("cls")
				continue
		print"1:Fate-grand_order"
		print ""
		print"2:Onmyouji"
		print ""
		print"3:Heartstone"
		print ""

		print"4:overwatch"
		print""
		a = input("Enter a number:")
		if a == 1:
			count = 0
			counta = 0
			countb = 0
			countc = 0
			countd = 0
			counte = 0
			countf = 0
			times = input("Please choose draw once or ten times:")
			def lottery():
				for i in xrange(times-1):
					yield random.randint(1,100)
			for random_number in lottery():
				x = random_number
				if x == 100:
					print"you get a 5 Stars Servant!"
					counta += 1
					count += 1
				elif 96<=x<=99:
					print"you get a 5 Stars Craft Essence!"
					countb += 1
					count += 1
				elif 93<=x<=95:
					print"you get a 4 Stars Servant!"
					countc += 1
					count += 1
				elif 81<=x<=92:
					print"you get a 4 Stars Craft Essence!"
					countd += 1
					count += 1
				elif 41<=x<=80:
					print"you get a 3 Stars Servent."
					counte += 1
					count += 1
				elif x<=40:
					print"you get a 3 Stars Craft Essense."
					countf += 1
			if count==0:
				def lottery():
					for o in xrange(1):
						yield random.randint(41,100)
				for random_number in lottery():
					x = random_number
					if x == 100:
						print"you get a 5 Stars Servant!"
						counta += 1
					elif 96<=x<=99:
						print"you get a 5 Stars Craft Essence!"
						countb += 1
					elif 93<=x<=95:
						print"you get a 4 Stars Servant!"
						countc += 1
					elif 81<=x<=92:
						print"you get a 4 Stars Craft Essence!"
						countd += 1
					elif 41<=x<=80:
						print"you get a 3 Stars Servent."
						counte += 1
			else:
				def lottery():
					for o in xrange(1):
						yield random.randint(1,100)
				for random_number in lottery():
					x = random_number
					if x == 100:
						print"you get a 5 Stars Servant!"
						counta += 1
					elif 96<=x<=99:
						print"you get a 5 Stars Craft Essence!"
						countb += 1
					elif 93<=x<=95:
						print"you get a 4 Stars Servant!"
						countc += 1
					elif 81<=x<=92:
						print"you get a 4 Stars Craft Essence!"
						countd += 1
					elif 41<=x<=80:
						print"you get a 3 Stars Servent."
						counte += 1
					elif x<=40:
						print"you get a 3 Stars Craft Essense."
						countf += 1
			print""
			print "you get %s five Stars Servant!"% counta
			print "you get %s five Stars Craft Essence!"% countb
			print "you get %s four Stars Servant!"% countc
			print "you get %s four Stars Craft Essence!"% countd
			print "you get %s three Stars Servant."% counte
			print "you get %s three Stars Craft Essence."% countf
			print ""
			countall += 1
			if times >= 20:
				t = 8
			else:
				t = 5
			print "program'll restart after %ss" % t
			time.sleep(t)
			os.system("cls")

		elif a == 2:
			countA = 0
			countB = 0
			countC = 0
			times = input("How many times do you want draw?:")
			def lottery():
				for i in xrange(times):
					yield random.randint(1,100)
			for random_number in lottery():
				x = random_number
				if x == 100:
					print"you get a ssr card!"
					countA += 1
				elif 91<=x<=99:
					print "you get a sr card!"
					countB += 1
				elif x<=90:
					print"you get a r card."
					countC += 1
			print""
			print "you get %s ssr card!"% countA
			print "you get %s sr card!"% countB
			print "you get %s r card!"% countC
			print ""
			countall += 1
			print "program'll restart after 5s"
			time.sleep(5)
			os.system("cls")

		elif a == 3:
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			count5 = 0
			count6 = 0
			count7 = 0
			count8 = 0
			times = input("Please enter the number of pack:")
			def lottery():
				for i in xrange(times * 5):
					yield random.randint(1,100000)
			for random_number in lottery():
				x = random_number
				if x >= 99889:
					print"you get a golden legendary card!"
					count1 += 1
				elif 99581<=x<=99888:
					print"you get a golden epic card!"
					count2 += 1
				elif 98311<=x<=99580:
					print"you get a golden rare card."
					count3 += 1
				elif 96741<=x<=98310:
					print"you get a golden common card."
					count4 += 1
				elif 95661<=x<=96740:
					print"you get a legendary card!"
					count5 += 1
				elif 91381<=x<=95660:
					print"you get an epic card!"
					count6 += 1
				elif 69981<=x<=91380:
					print"you get a rare card."
					count7 += 1
				else:
					print"you get a common card."
					count8 += 1
			print""
			print"you get %s golden legendary card!"% count1
			print"you get %s golden epic card!"% count2
			print"you get %s golden rare card."% count3
			print"you get %s golden common card."% count4
			print"you get %s legendary card!"% count5
			print"you get %s epic card!"% count6
			print"you get %s rare card."% count7
			print"you get %s common card."% count8
			print ""
			countall += 1
			if times >= 15:
				t = 8
			else:
				t = 5
			print "program'll restart after %ss" % t
			time.sleep(t)
			os.system("cls")

		elif a == 4:
			count_l = 0
			count_e = 0
			count_r = 0
			count_c = 0
			times = input("Please choose number of boxes:")
			def lottery():
				for i in xrange(times*4):
					yield random.randint(1,21059)
			for random_number in lottery():
				x = random_number
				if x >= 20131:
					print"you get a legendary item!"
					count_l += 1
				elif 17530<=x<=20130:
					print "you get an epic item!"
					count_e += 1
				elif 9708<=x<=17539:
					print"you get a rare item."
					count_r += 1
				elif x<=9707:
					print"you get a common item."
					count_c += 1
			print""
			print"you get %s legendary item!"% count_l
			print"you get %s epic item!"% count_e
			print"you get %s rare item!"% count_r
			print"you get %s common item!"% count_c
			print ""
			countall += 1
			print "program'll restart after 8s"
			time.sleep(5)
			os.system("cls")
		else:
			countall += 1
			print"don't enter wrong number!"
			time.sleep(3)
			os.system("cls")
			break
	continue
