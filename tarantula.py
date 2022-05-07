from rich.console import Console
from rich.panel import Panel
from rich import box
import os
from twoip import TwoIP

console = Console()

def getGeo(ip):
	twoip = TwoIP(key=None)
	geo = twoip.geo(ip=ip)
	return geo

def getProvider(ip):
	twoip = TwoIP()
	provider = twoip.provider(ip=ip)
	return provider



if __name__ == '__main__':
	os.system('clear')
	console.print(Panel.fit('''████████╗░█████╗░██████╗░░█████╗░███╗░░██╗████████╗██╗░░░██╗██╗░░░░░░█████╗░
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗
░░░██║░░░███████║██████╔╝███████║██╔██╗██║░░░██║░░░██║░░░██║██║░░░░░███████║
░░░██║░░░██╔══██║██╔══██╗██╔══██║██║╚████║░░░██║░░░██║░░░██║██║░░░░░██╔══██║
░░░██║░░░██║░░██║██║░░██║██║░░██║██║░╚███║░░░██║░░░╚██████╔╝███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝''', style='yellow', box=box.HEAVY))
	console.print(Panel.fit('{1}GET GEO \n{2}GET PROVIDER INFO \n{3}MAIN INFO \n{4}EXIT', style='bold magenta', box=box.DOUBLE))

	while True:
		try:
			choose = int(console.input('[blink magenta]>>>[/]'))

			if choose == 1:
				targ = console.input("[green]TARGET IP: [/]")
				data = getGeo(targ)

				console.print(Panel.fit(f'''COUNTRY: [italic magenta]{data["country"]}[/]
*--------------------------------*
CITY: [italic magenta]{data["city"]}[/]
*--------------------------------*
REGION: [italic magenta]{data["region"]}[/]
*--------------------------------*
COORDINATES:
  LONGITUDE: [italic magenta]{data["longitude"]}[/]
  LATITUDE: [italic magenta]{data["latitude"]}[/]
*--------------------------------*
TIME ZONE: [italic magenta]{data["time_zone"]}[/]
*--------------------------------*
ZIP CODE: [italic magenta]{data["zip_code"]}[/]''', style='green', box=box.ASCII))


			elif choose == 2:
				targ = console.input("[green]TARGET IP: [/]")
				data = getProvider(targ)

				console.print(Panel.fit(f'''IP RANGE START: [italic magenta]{data["ip_range_start"]}[/]
*--------------------------------*
IP RANGE END: [italic magenta]{data["ip_range_end"]}[/]
*--------------------------------*
MASK: [italic magenta]{data["mask"]}[/]
*--------------------------------*
NAME RIPE: [italic magenta]{data["name_ripe"]}[/]
*--------------------------------*
ROUTE: [italic magenta]{data["route"]}[/]''', style='green', box=box.ASCII))


			elif choose == 3:
				console.print(Panel.fit('''
TARANTULA - ALTERNATIVE OF IP TRACER
MADE BY: [italic magenta]blueTUZZ_01[/]
TEAM: [italic magenta]The361[/]
GITHUB: [italic magenta]https://github.com/blueTUZZ01[/]
				''', style='green', box=box.HEAVY))

			elif choose == 4:
				break
			

		except RuntimeError:
			console.print("CAN'T DO THIS, SORRY", style='blink red')
		except:
			console.print("WRONG", style='red')
			pass