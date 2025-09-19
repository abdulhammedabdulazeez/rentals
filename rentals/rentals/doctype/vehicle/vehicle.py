# Copyright (c) 2025, HamidDev and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
    def validate(self):
        """Validate the vehicle document before saving."""
        self.set_title()

    def set_title(self):
        """Set the title of the vehicle based on its make, model, and year."""
        self.title = f"{self.make} {self.model} ({self.year})"
