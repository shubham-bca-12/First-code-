"""

PROJECT: Seth Ji BBA Portfolio System
AUTHOR: Shubham | KNIMT Sultanpur BBA 2026
VERSION: 1.0
DESCRIPTION: BBA student ka personal data + KNIMT calculator
DADA JI KA AASHIRWAD: Included ☕👑

"""

import datetime

# ==================== CLASS BANAYI ====================
class SethJiBBA:
    """
    KNIMT Sultanpur ka BBA Student
    Future Crorepati ka official record
    """
    
    def __init__(self, naam, umar, college):
        self.naam = naam
        self.umar = umar
        self.college = college
        self.admission_year = 2026
        self.skills = ["Business", "Python Basic", "GitHub"]
        self.dada_ji_ka_aashirwad = True
    
    def introduction(self):
        """Seth ji ka parichay"""
        print("=" * 50)
        print(f"🔥 NAMASTE, MAIN {self.naam.upper()} 🔥")
        print("=" * 50)
        print(f"📚 College: {self.college}")
        print(f"🎂 Umar: {self.umar} saal")
        print(f"📅 Admission: {self.admission_year}")
        print(f"💻 Skills: {', '.join(self.skills)}")
        print(f"🙏 Dada Ji Ka Aashirwad: {self.dada_ji_ka_aashirwad}")
        print("=" * 50)
    
    def knimt_fees_calculator(self):
        """KNIMT vs KNIPSS ka fayda calculator"""
        print("\n💰 KNIMT FEES CALCULATOR 💰")
        knimt_total = 67000
        knipss_total = 112000
        
        print(f"KNIMT BBA 3 Saal: ₹{knimt_total:,}")
        print(f"KNIPSS BBA 3 Saal: ₹{knipss_total:,}")
        
        bachat = knipss_total - knimt_total
        per_year_bachat = bachat / 3
        per_month_bachat = bachat / 36
        
        print(f"\n✅ TOTAL BACHAT: ₹{bachat:,}")
        print(f"✅ Per Year Bachat: ₹{per_year_bachat:,.0f}")
        print(f"✅ Per Month Bachat: ₹{per_month_bachat:,.0f}")
        
        if bachat > 40000:
            print("🔥 SETH JI KA DIMAG = PROFIT 🔥")
        
        return bachat
    
    def future_plan(self):
        """4 Saal ka plan"""
        print("\n📈 4 SAAL KA SETH JI PLAN 📈")
        current_year = datetime.datetime.now().year
        
        for saal in range(4):
            year = current_year + saal
            if saal == 0:
                print(f"{year}: BBA 1st Year + Python + Job ✅")
            elif saal == 1:
                print(f"{year}: BBA 2nd Year + Freelancing ₹10K/month ✅")
            elif saal == 2:
                print(f"{year}: BBA 3rd Year + ₹25K Job + GitHub 50 Repo ✅")
            else:
                print(f"{year}: GRADUATE + ₹60K+ Job + Seth Ji 👑")
    
    def dada_ji_ka_mantra(self):
        """Motivation"""
        mantras = [
            "Puttar mehnat kar, paisa jhakk maar ke aayega 💰",
            "Time barbad mat kar, code kar ya padh 📚",
            "GitHub pe green box roz bhar, naukri pakki 🟩",
            "KNIMT le liya, ab crorepati banna tera kaam 👑"
        ]
        print("\n☕ DADA JI KA MANTRA ☕")
        for i, mantra in enumerate(mantras, 1):
            print(f"{i}. {mantra}")

# ==================== CODE CHALAO ====================
if __name__ == "__main__":
    # Seth ji ka object banaya
    shubham = SethJiBBA(
        naam="Shubham", 
        umar=16, 
        college="KNIMT Sultanpur"
    )
    
    # Sab function chala diye
    shubham.introduction()
    bachat = shubham.knimt_fees_calculator()
    shubham.future_plan()
    shubham.dada_ji_ka_mantra()
    
    print("\n" + "=" * 50)
    print("🎉 CODE SUCCESSFULLY RUN HO GAYA 🎉")
    print(f"💸 AAJ KA FAYDA: ₹{bachat:,} Bachaya")
    print("GitHub: github.com/shubham-bca-12")
    print("=" * 50)
