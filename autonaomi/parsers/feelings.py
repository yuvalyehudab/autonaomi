#feelings.py
#autonaomi.parsers

def feelings(snapshot, path):
	return {
		'thirst': snapshot.feelings.thirst,
		'happiness': snapshot.feelings.happiness,
		'exhaustion': snapshot.feelings.exhaustion,
		'hunger': snapshot.feelings.hunger
	}