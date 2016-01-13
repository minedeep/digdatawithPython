from django.shortcuts import render_to_response 

digit_num_str = {
		"1": "  \n  |\n  |",
		"2": " _\n _|\n|_ ",
		"3": " _\n _|\n _|",
		"4": "  \n|_|\n  |",
		"5": " _\n|_ \n _|",
		"6": " _\n|_ \n|_|",
		"7": " _\n  |\n  |",
		"8": " _\n|_|\n|_|",
		"9": " _\n|_|\n  |",
		"0": " _\n| |\n|_|",
		"A": " _\n|_|\n| |",
		"B": " _\n|_|\n|_|",
		"C": " _\n|  \n|_ ",
		"D": " _\n| |\n|_|",
		"E": " _\n|_ \n|_ ",
		"F": " _\n|_ \n|  ",
		"G": " _\n|_ \n|_|",
		"H": "  \n|_|\n| |",
		"I": "  \n  |\n  |",
		"J": "  \n  |\n _|",
		"K": "  \n|/ \n|\ ",
		"L": "  \n|  \n|_ ",
		}
def seven_segment_number(request):
	query = request.GET.get('q', '')
	if query:
		str_display_list = []
		# parse the query string to know what to display, a number or a character
		for i in range(0, len(query)):
			# if character
			if query[i].isalpha():
				tmpstr = query[i].upper()
			else:
				tmpstr = query[i]
			# look up the formatted string from the digit_num_str 
			# for the corresponding character or number
			if not tmpstr.isspace() and digit_num_str.has_key(tmpstr):
				tmpstr = digit_num_str[tmpstr]
				str_display_list.append(tmpstr.split("\n"))
		# convert the str_display_list to a string to be displayed
		str_to_display = ""
		for i in range(0, 3):
			for j in range(0, len(str_display_list)):
				str_to_display += str_display_list[j][i]
				str_to_display += " "
				if i == 0 :
					str_to_display += " "
			str_to_display += "\n"
	else:
		str_to_display = ""

	return render_to_response('seven_segment_number.html', {'number_to_display':query, 'str_to_display':str_to_display})




