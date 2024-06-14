import os
import time
import sys
os.system("clear")
print("""\033[1;34;40m

░██████╗░░█████╗░░██████╗░██████╗░██╗░░░██╗██████╗░██╗░░░██╗
██╔════╝░██╔══██╗██╔════╝██╔════╝░██║░░░██║██╔══██╗██║░░░██║
██║░░██╗░███████║╚█████╗░██║░░██╗░██║░░░██║██████╔╝██║░░░██║
██║░░╚██╗██╔══██║░╚═══██╗██║░░╚██╗██║░░░██║██╔══██╗██║░░░██║
╚██████╔╝██║░░██║██████╔╝╚██████╔╝╚██████╔╝██║░░██║╚██████╔╝
░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚═════╝░░╚═════╝░╚═╝░░╚═╝░╚═════╝░
""")
print("""\033[1;33;40m[+] Created by Solomon Adenuga
[✓] GasGuru v1.0 is a tool for solving gas laws based questions""")
def Boyles_law():
	print("\nSIMPLY SKIP ANY PARAMETER THAT IS NOT GIVEN,THE PARAMETER YOU SKIP IS WHAT THIS PROGRAM WILL SOLVE FOR")
	formula = input("Enter 's' for a single gas question or 'd' for double gases: ")
	if formula.lower().strip() == "s":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				p = input(" P:").strip()
				v = input(" V:").strip()
				k = input(" K:").strip()
				if p == "":
					p = float(k) / float(v)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n P: {p:,.2f}")
				elif v == "":
					v = float(k) / float(p)
					print("\033[92m`  Calculating.....")
					time.sleep(2)
					print(f"\n V: {v:,.2f}")
				elif k == "":
					k = float(p) * float(v)
					print("\033[92m`  Calculating.....")
					time.sleep(2)
					print(f"\n K: {k:,.2f}")
				valid = True
			except(ValueError, TypeError):
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
	elif formula.lower().strip() == "d":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				p1 = input(" P1: ").strip()
				v1 = input(" V1: ").strip()
				p2 = input(" P2: ").strip()
				v2 = input(" V2: ").strip()
				if p1 == "":
					p1 = (float(p2) * float(v2)) / float(v1)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n P1: {p1:,.2f}")
				elif v1 == "":
					v1 = (float(p2) * float(v2)) / float(p1)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n V1: {v1:,.2f}")
				elif p2 == "":
					p2 = (float(p1) * float(v1)) / float(v2)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n P2: {p2:,.2f}")
				elif v2 == "":
					v2 = (float(p1) * float(v1)) / float(p2)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n V2: {v2:,.2f}")
					valid = True
			except (ValueError,TypeError):
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
def Charles_law():
	print("\n SIMPLY SKIP ANY PARAMETER THAT IS NOT GIVEN,THE PARAMETER YOU SKIP IS WHAT THIS PROGRAM WILL SOLVE FOR")
	formula = input(" Enter 's' for single gas question or 'd' for double gas: ")
	if formula.lower().strip() == "s":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				v = input(" V:").strip()
				k = input(" K: ").strip()
				t = input(" T: ").strip()
				if v == "":
					v = float(k) * (float(t) + 273)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n V: {v:,.2f}")
				elif k == "":
					k = float(v) / (float(t) +273)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n K: {k:,.2f}")
				elif t == "":
					t = float(v) / float(k)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n T: {t:,.2f}")
				valid = True
			except (ValueError,TypeError):
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
	elif formula.lower().strip() == "d":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				v1 = input(" V1:").strip()
				t1 = input(" T1(in degree celsius):").strip()
				v2 = input(" V2:").strip()
				t2 = input(" T2(in degree celsius):").strip()
				if v1 == "":
					v1 = (float(v2) * (float(t1) + 273)) / (float(t2) +273)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n V1: {v1:,.2f}")
				elif t1 == "":
					t1 = (float(v1) * (float(t2) + 273)) / float(v2)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n T1: {t1:,.2f}K")
				elif v2 == "":
					v2 = (float(v1) * (float(t2) +273)) / (float(t1) + 273)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n V2: {v2:,.2f}")
				elif t2 == "":
					t2 = (float(v2) * (float(t1) + 273)) / float(v1)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n T2: {t2:,.2f}K")
				valid = True
			except (ValueError,TypeError):
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")

def General_gas_equation():
	print("\n SIMPLY SKIP ANY PARAMETER THAT IS NOT GIVEN,THE PARAMETER YOU SKIP IS WHAT THIS PROGRAM WILL SOLVE FOR")
	formula = input(" Enter 's' for a single gas question or 'd' for double gases: ")
	if formula.lower().strip() == "s":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				p = input(" P:").strip()
				v = input(" V:").strip()
				t = input(" T(in degree celsius):").strip()
				k = input(" K:").strip()
				if p == "":
					p = (float(k) * (float(t) + 273)) / float(v)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n P: {p:,.2f}")
				elif v == "":
					v = (float(k) * (float(t) + 273)) / float(p)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n V: {v:,.2f}")
				elif t == "":
					t = (float(p) * float(v)) / float(k)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n T: {t:,.2f}")
				elif k == "":
					k = (float(p) * float(v)) / (float(t) + 273)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f"\n K: {k:,.2f}")
				valid = True
			except (ValueError,TypeError):
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
	elif formula.lower().strip() == "d":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				p1 = input(" P1;").strip()
				v1 = input(" V1:").strip()
				t1 = input(" T1(in degree celsius):").strip()
				p2 = input(" P2:").strip()
				v2 = input(" V2:").strip()
				t2 = input(" T2(in degree celsius):")
				if p1 == "":
					p1 = (float(p2) * float(v2) * (float(t1) + 273)) / (float(v1) * (float(t2) + 273))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" P1: {p1:,.2f}")
				elif v1 == "":
					v1 = (float(p2) * float(v2) * (float(t1) + 273)) / (float(p1) * (float(t2) + 273))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" V1: {v1:,.2f}")
				elif t1 == "":
					t1 = (float(p1) * float(v1) * (float(t2) + 273)) / (float(p2) * float(v2))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" T1: {t1:,.2f}K")
				elif p2 == "":
					p2 = (float(p1) * float(v1) * (float(t2) + 273)) / (float(v2) * (float(t1) + 273))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" P2: {p2:,.2f}")
				elif v2 == "":
					v2 = (float(p1) * float(v1) * (float(t2) + 273)) / (float(p2) * (float(t1) + 273))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" V2: {v2:,.2f}")
				elif t2 == "":
					t2 = (float(p2) * float(v2) * (float(t1) + 273)) / (float(p1) * float(v1))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" T2: {t2:,.2f}K")
				valid = True
			except ValueError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")

def ideal_gas_equation():
	print("\n SIMPLY SKIP ANY PARAMETER THAT IS NOT GIVEN,THE PARAMETER YOU SKIP IS WHAT THIS PROGRAM WILL SOLVE FOR")
	formula = input(" Enter 's' for a single gas question or 'd' for double gases:")
	if formula.lower().strip() == "s":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				p = input(" P:").strip()
				v = input(" V:").strip()
				n = input(" N:").strip()
				r = input(" R:").strip()
				t = input(" T:").strip()
				if p == "":
					p = (float(n) * float(r) * (float(t) + 273)) / float(v)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" P: {p:,.2f}")
				elif v == "":
					v = (float(n) * float(r) * (float(t) + 273)) / float(p)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" V: {v:,.2f}")
				elif n == "":
					t = float(t) + 273
					n = (float(p) * float(v)) / (float(r) * t)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" N: {n:,.2f} mol")
				elif r == "":
					r = (float(p) * float(v)) / (float(n) * (float(t) + 273))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" R: {r:,.2f}")
				elif t == "":
					t = (float(p) * float(v)) / (float(n) * float(r))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" T: {t:,.2f}")
					valid = True
			except ValueError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
	elif formula.lower().strip() == "d":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				p1 = input(" P1:").strip()
				v1 = input(" V1:").strip()
				n1 = input(" N1:").strip()
				t1 = input(" T1:").strip()
				p2 = input(" P2:").strip()
				v2 = input(" V2:").strip()
				n2 = input(" N2:").strip()
				t2 = input(" T2:").strip()
				if p1 == "":
					t1 = float(t1) + 273
					t2 = float(t2) + 273
					p1 = (float(p2) * float(v2) * float(n1) * t1) / (float(v1) * float(n2) * t2)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" P1: {p1:,.2f}")
				elif v1 == "":
					t1 = float(t1) + 273
					t2 = float(t2) + 273
					v1 = (float(p2) * float(v2) * float(n1) * t1) / (float(p1) * float(n2) * t2)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" V1: {v1:,.2f}")
				elif n1 == "":
					t1 = float(t1) + 273
					t2 = float(t2) + 273
					n1 = (float(p1) * float(v1) * float(n2) * t2) / (float(p2) * float(v2) * t1)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" N1: {n1:,.2f}mol")
				elif t1 == "":
					t2 = float(t2) + 273
					t1 = (float(p1) * float(v1) * float(n2) * t2) / (float(p2) * float(v2) * float(n1))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" T1: {t1:,.2f}K")
				elif p2 == "":
					t1 = float(t1) + 273
					t2 = float(t2) + 273
					p2 = (float(p1) * float(v1) * float(n2) * t2) / (float(v2) * float(n1) * t1)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" P2: {p2:,.2f}")
				elif v2 == "":
					t1 = float(t1) + 273
					t2 = float(t2) + 273
					v2 = (float(p1) * float(v1) * float(n2) * t2) / (float(p2) * float(n1) * float(t1))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" V2: {v2:,.2f}")
				elif n2 == "":
					t1 = float(t1) + 273
					t2 = float(t2) + 273
					n2 = (float(p2) * float(v2) * float(n1) * t1) / (float(p1) * float(v1) * float(t2))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" N2: {n2:,.2f}mol")
				elif t2 == "":
					t1 = float(t1) + 273
					t2 = (float(p2) * float(v2) * float(n1) * t1) / (float(p1) * float(v1) * float(n2))
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" T2: {t2:,.2f}K")
				valid = True
			except ValueError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")

def Grahams_law():
	print("\n SIMPLY SKIP ANY PARAMETER THAT IS NOT GIVEN,THE PARAMETER YOU SKIP IS WHAT THIS PROGRAM WILL SOLVE FOR")
	formula = input(" Enter 's' for single gas question or 'd' for double gases:")
	if formula.lower().strip() == "s":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				r = input(" R:")
				k = input(" K:")
				mm = input(" Mm:")
				if r.strip() == "":
					r = float(k) / float(mm)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" R: {r:,.2f}")
				elif k.strip() == "":
					k = float(r) * float(mm)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" K: {k:,.2f}")
				elif mm.strip() == "":
					mm = float(k) / float(r)
					print("\033[92m`  Calculating.....")
					time.sleep(2)
					print(f" Mm: {mm:,.2f}")
				valid = True
			except ValueError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
	elif formula.lower().strip() == "d":
		valid = False
		while not valid:
			try:
				print("\033[1;36;40m")
				r1 = input(" R1:").strip()
				r2 = input(" R2:").strip()
				mm1 = input(" Mm1:").strip()
				mm2 = input(" Mm2:").strip()
				if r1 == "":
					r1 = (float(r2) * (float(mm2) ** 0.5)) / (float(mm1) ** 0.5)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" R1: {r1:,.2f}")
				elif r2 == "":
					r2 = (float(r1) * (float(mm1) ** 0.5)) / (float(mm2) ** 0.5)
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" R2: {r2:,.2f}")
				elif mm1 == "":
					mm1 = ((float(r2) * (float(mm2) ** 0.5)) / float(r1)) ** 2
					print("\033[92m`  Calculating....")
					time.sleep(2)
					print(f" Mm1: {mm1:,.2f}")
				elif mm2 == "":
					mm2 = ((float(r1) * (float(mm1) ** 0.5)) / float(r2)) ** 2
					print("\033[92m`  Calculating.....")
					time.sleep(2)
					print(f" Mm2: {mm2:,.2f}")
				valid = True
			except (ValueError, TypeError):
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
def program_intro():
	print("\n")
	print("\033[1;33;40m")
	print("*******" * 10)
	print("\033[1;36;40mLoading....")
	sys.stdout.write('\r' + ' ' * 7 + '\r')
	time.sleep(3)
	print("""  \033[92m` 
	[1.] Boyle's Law
	[2.] Charle's Law
	[3.] General Gas Equation
	[4.] Ideal Gas Equation
	[5.] Dalton's Law of partial pressure (coming soon...)
	[6.] Graham's Law of Diffusion
	[7 ] Exit the program
	""")
	print("\033[1;33;40m")
	print("*******" * 10)
	response = input("\033[1;36;40m Enter a number:")
	if response == "1":
		time.sleep(1)
		Boyles_law()
	elif response == "2":
		time.sleep(1)
		Charles_law()
	elif response == "3":
		time.sleep(1)
		General_gas_equation()
	elif response == "4":
		time.sleep(1)
		ideal_gas_equation()
	elif response == "5":
		time.sleep(2)
		print("\033[1;33;40m Coming soon...")
	elif response == "6":
		time.sleep(1)
		Grahams_law()
	elif response == "7":
		time.sleep(2)
		print("\033[1;31;40m OPERATION CANCELLED!")
		sys.exit()

while True:
	program_intro()