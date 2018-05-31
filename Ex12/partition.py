import re

def partition(players):
	exp = re.compile("^[A-Ma-m]")
	return list(filter(exp.match, players))