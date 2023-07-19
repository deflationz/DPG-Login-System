import dearpygui.dearpygui as dpg
data_user = 'admin'
data_password = 'password'
dpg.create_context()
with dpg.window(label='Login', no_collapse=True, no_resize=True, no_close=True, tag='login', show=True):
	dpg.set_primary_window('login', True)
	dpg.add_text('Username:')
	username = dpg.add_input_text()
	dpg.add_text('Password:')
	password = dpg.add_input_text(password=True)
	dpg.add_text('')
	def login_func(user, passs):
		iss = False
		if user == data_user:
			iss = True
		if passs == data_password:
			if iss == True:
				dpg.configure_item('blank', default_value='Correct!')
		else:
			dpg.configure_item('blank', default_value='Incorrect credentials... Try again')
			pass
	dpg.add_button(label='Login', callback=lambda:login_func(user=dpg.get_value(username), passs=dpg.get_value(password)))
	dpg.add_text('', tag='blank')
dpg.create_viewport(title='Login System', width=835, height=697)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
