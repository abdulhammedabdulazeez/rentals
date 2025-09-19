# Copyright (c) 2025, HamidDev and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"
		self.full_name = self.full_name.strip()


# API SECRET KEY: 2bac7d05699ab47

# Abdulhammed token: 6d0233fa080a8fe:acfbc4fbafb069c