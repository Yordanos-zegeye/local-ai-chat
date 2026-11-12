
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
import os

os.makedirs("documents", exist_ok=True)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "CustomTitle",
    parent=styles["Title"],
    textColor=colors.HexColor("#1D4ED8"),
    spaceAfter=20
)

heading = styles["Heading2"]
body = styles["BodyText"]

documents = {
    "01_Startup_Business_Plan.pdf": {
        "title": "GreenBasket Startup Business Plan",
        "sections": [
            ("Business Overview",
             "GreenBasket is a fictional startup founded in 2025. "
             "It provides online grocery delivery services, connecting "
             "local farmers with urban consumers."),

            ("Business Model",
             "GreenBasket earns revenue through delivery fees and "
             "commissions from partner farmers. The delivery fee is "
             "150 ETB per order. The company charges farmers a "
             "10 percent commission on completed sales."),

            ("Target Customers",
             "The primary customers are urban households, working "
             "professionals, restaurants and small grocery retailers."),

            ("Products",
             "The platform sells fresh vegetables, fruits, grains, "
             "dairy products and locally sourced organic food."),

            ("Business Objectives",
             "The startup aims to reach 2,000 monthly active customers "
             "within its first year and partner with 50 local farmers."),

            ("Operations",
             "The company operates from Addis Ababa and uses three "
             "delivery motorcycles. Orders are received through a "
             "mobile application and website."),

            ("Initial Investment",
             "The founders invested 1,500,000 ETB to establish the "
             "business. The investment covered technology development, "
             "delivery equipment and initial marketing.")
        ]
    },

    "02_Financial_Report.pdf": {
        "title": "GreenBasket Financial Report",
        "sections": [
            ("Monthly Revenue",
             "The company's average monthly revenue is 450,000 ETB. "
             "Revenue comes from delivery fees and farmer commissions."),

            ("Monthly Expenses",
             "Employee salaries: 120,000 ETB. "
             "Office rent: 25,000 ETB. "
             "Fuel and transportation: 40,000 ETB. "
             "Marketing: 35,000 ETB. "
             "Technology and hosting: 15,000 ETB. "
             "Other expenses: 15,000 ETB."),

            ("Total Monthly Expenses",
             "Total monthly operating expenses are 250,000 ETB."),

            ("Monthly Operating Profit",
             "Monthly operating profit before taxes is 200,000 ETB, "
             "calculated as revenue minus operating expenses."),

            ("Annual Projection",
             "If monthly revenue and expenses remain constant, "
             "annual revenue will be 5,400,000 ETB and annual "
             "operating expenses will be 3,000,000 ETB. "
             "Projected annual operating profit is 2,400,000 ETB."),

            ("Funding Requirements",
             "GreenBasket is seeking an additional investment of "
             "2,000,000 ETB to expand delivery operations and "
             "improve its technology platform."),

            ("Financial Risk",
             "The major financial risks include fuel price increases, "
             "customer acquisition costs and seasonal fluctuations "
             "in agricultural supply.")
        ]
    },

    "03_Marketing_Strategy.pdf": {
        "title": "GreenBasket Marketing Strategy",
        "sections": [
            ("Marketing Objectives",
             "GreenBasket aims to acquire 2,000 monthly active customers "
             "during its first year of operation."),

            ("Target Market",
             "The target market consists of urban consumers aged "
             "22 to 45, particularly working professionals and "
             "families living in Addis Ababa."),

            ("Digital Marketing",
             "The company uses Facebook, Instagram and Telegram "
             "to promote its products and communicate with customers."),

            ("Marketing Budget",
             "The monthly marketing budget is 35,000 ETB. "
             "Facebook advertising receives 15,000 ETB, "
             "influencer marketing receives 8,000 ETB, "
             "content production receives 7,000 ETB and "
             "promotional activities receive 5,000 ETB."),

            ("Customer Acquisition",
             "The company offers a 20 percent discount on the "
             "first order for new customers. Customers who refer "
             "a friend receive a 100 ETB delivery credit."),

            ("Competitive Advantage",
             "GreenBasket differentiates itself through direct "
             "relationships with local farmers, transparent pricing "
             "and reliable delivery services."),

            ("Performance Indicators",
             "The company measures customer acquisition cost, "
             "customer retention rate, monthly active users, "
             "conversion rate and average order value."),

            ("Marketing Channels",
             "The primary marketing channels are social media, "
             "referral campaigns, local partnerships and email marketing.")
        ]
    }
}

for filename, data in documents.items():

    path = os.path.join("documents", filename)

    pdf = SimpleDocTemplate(
        path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    content = [
        Paragraph(data["title"], title_style),
        Spacer(1, 15)
    ]

    for section_title, text in data["sections"]:
        content.append(Paragraph(section_title, heading))
        content.append(Spacer(1, 6))
        content.append(Paragraph(text, body))
        content.append(Spacer(1, 15))

    pdf.build(content)

    print(f"Created: {path}")

print("\nAll three test PDFs generated successfully!")
