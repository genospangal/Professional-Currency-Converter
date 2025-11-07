import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime
import threading

class CurrencyConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Professional Currency Converter")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Currency codes for 150+ countries
        self.currencies = {
            'USD': 'United States Dollar',
            'EUR': 'Euro',
            'GBP': 'British Pound Sterling',
            'JPY': 'Japanese Yen',
            'AUD': 'Australian Dollar',
            'CAD': 'Canadian Dollar',
            'CHF': 'Swiss Franc',
            'CNY': 'Chinese Yuan',
            'SEK': 'Swedish Krona',
            'NZD': 'New Zealand Dollar',
            'MXN': 'Mexican Peso',
            'SGD': 'Singapore Dollar',
            'HKD': 'Hong Kong Dollar',
            'NOK': 'Norwegian Krone',
            'KRW': 'South Korean Won',
            'INR': 'Indian Rupee',
            'RUB': 'Russian Ruble',
            'ZAR': 'South African Rand',
            'BRL': 'Brazilian Real',
            'PLN': 'Polish Złoty',
            'DKK': 'Danish Krone',
            'CZK': 'Czech Koruna',
            'HUF': 'Hungarian Forint',
            'THB': 'Thai Baht',
            'TRY': 'Turkish Lira',
            'RON': 'Romanian Leu',
            'BGN': 'Bulgarian Lev',
            'HRK': 'Croatian Kuna',
            'ISK': 'Icelandic Króna',
            'AED': 'UAE Dirham',
            'SAR': 'Saudi Riyal',
            'QAR': 'Qatari Riyal',
            'KWD': 'Kuwaiti Dinar',
            'BHD': 'Bahraini Dinar',
            'OMR': 'Omani Rial',
            'JOD': 'Jordanian Dinar',
            'LBP': 'Lebanese Pound',
            'EGP': 'Egyptian Pound',
            'MAD': 'Moroccan Dirham',
            'TND': 'Tunisian Dinar',
            'DZD': 'Algerian Dinar',
            'LYD': 'Libyan Dinar',
            'SDG': 'Sudanese Pound',
            'ETB': 'Ethiopian Birr',
            'KES': 'Kenyan Shilling',
            'UGX': 'Ugandan Shilling',
            'TZS': 'Tanzanian Shilling',
            'RWF': 'Rwandan Franc',
            'GHS': 'Ghanaian Cedi',
            'NGN': 'Nigerian Naira',
            'XOF': 'West African CFA Franc',
            'XAF': 'Central African CFA Franc',
            'ZMW': 'Zambian Kwacha',
            'BWP': 'Botswanan Pula',
            'SZL': 'Swazi Lilangeni',
            'LSL': 'Lesotho Loti',
            'MUR': 'Mauritian Rupee',
            'SCR': 'Seychellois Rupee',
            'MGA': 'Malagasy Ariary',
            'KMF': 'Comorian Franc',
            'DJF': 'Djiboutian Franc',
            'SOS': 'Somali Shilling',
            'ERN': 'Eritrean Nakfa',
            'AFN': 'Afghan Afghani',
            'PKR': 'Pakistani Rupee',
            'LKR': 'Sri Lankan Rupee',
            'NPR': 'Nepalese Rupee',
            'BTN': 'Bhutanese Ngultrum',
            'BDT': 'Bangladeshi Taka',
            'MVR': 'Maldivian Rufiyaa',
            'MMK': 'Myanmar Kyat',
            'LAK': 'Lao Kip',
            'KHR': 'Cambodian Riel',
            'VND': 'Vietnamese Dong',
            'IDR': 'Indonesian Rupiah',
            'MYR': 'Malaysian Ringgit',
            'BND': 'Brunei Dollar',
            'PHP': 'Philippine Peso',
            'TWD': 'New Taiwan Dollar',
            'MOP': 'Macanese Pataca',
            'MNT': 'Mongolian Tögrög',
            'KZT': 'Kazakhstani Tenge',
            'KGS': 'Kyrgyzstani Som',
            'TJS': 'Tajikistani Somoni',
            'UZS': 'Uzbekistani Som',
            'TMT': 'Turkmenistani Manat',
            'AZN': 'Azerbaijani Manat',
            'GEL': 'Georgian Lari',
            'AMD': 'Armenian Dram',
            'BYN': 'Belarusian Ruble',
            'UAH': 'Ukrainian Hryvnia',
            'MDL': 'Moldovan Leu',
            'ALL': 'Albanian Lek',
            'MKD': 'Macedonian Denar',
            'RSD': 'Serbian Dinar',
            'BAM': 'Bosnia-Herzegovina Convertible Mark',
            'EUR': 'Euro (Montenegro)',
            'ILS': 'Israeli New Shekel',
            'CYP': 'Cyprus Pound',
            'MTL': 'Maltese Lira',
            'SIT': 'Slovenian Tolar',
            'SKK': 'Slovak Koruna',
            'EEK': 'Estonian Kroon',
            'LVL': 'Latvian Lats',
            'LTL': 'Lithuanian Litas',
            'FIM': 'Finnish Markka',
            'IEP': 'Irish Pound',
            'ITL': 'Italian Lira',
            'ESP': 'Spanish Peseta',
            'PTE': 'Portuguese Escudo',
            'FRF': 'French Franc',
            'BEF': 'Belgian Franc',
            'NLG': 'Dutch Guilder',
            'LUF': 'Luxembourg Franc',
            'ATS': 'Austrian Schilling',
            'DEM': 'German Mark',
            'GRD': 'Greek Drachma',
            'CLP': 'Chilean Peso',
            'ARS': 'Argentine Peso',
            'UYU': 'Uruguayan Peso',
            'PYG': 'Paraguayan Guaraní',
            'BOB': 'Bolivian Boliviano',
            'PEN': 'Peruvian Sol',
            'COP': 'Colombian Peso',
            'VES': 'Venezuelan Bolívar',
            'GYD': 'Guyanese Dollar',
            'SRD': 'Surinamese Dollar',
            'FKP': 'Falkland Islands Pound',
            'BMD': 'Bermudian Dollar',
            'BSD': 'Bahamian Dollar',
            'BBD': 'Barbadian Dollar',
            'JMD': 'Jamaican Dollar',
            'KYD': 'Cayman Islands Dollar',
            'TTD': 'Trinidad and Tobago Dollar',
            'DOP': 'Dominican Peso',
            'HTG': 'Haitian Gourde',
            'CUP': 'Cuban Peso',
            'NIO': 'Nicaraguan Córdoba',
            'CRC': 'Costa Rican Colón',
            'PAB': 'Panamanian Balboa',
            'GTQ': 'Guatemalan Quetzal',
            'BZD': 'Belize Dollar',
            'HNL': 'Honduran Lempira',
            'SVC': 'Salvadoran Colón',
            'AWG': 'Aruban Florin',
            'ANG': 'Netherlands Antillean Guilder',
            'XCD': 'East Caribbean Dollar',
            'TOP': 'Tongan Paʻanga',
            'WST': 'Samoan Tālā',
            'VUV': 'Vanuatu Vatu',
            'SBD': 'Solomon Islands Dollar',
            'NCL': 'New Caledonian Franc',
            'FJD': 'Fijian Dollar',
            'PGK': 'Papua New Guinean Kina',
            'TVD': 'Tuvaluan Dollar',
            'NRU': 'Nauruan Dollar',
            'KID': 'Kiribati Dollar',
            'MHL': 'Marshallese Dollar',
            'PWD': 'Palauan Dollar',
            'FSM': 'Micronesian Dollar'
        }
        
        self.exchange_rates = {}
        self.last_update = None
        
        self.setup_ui()
        self.update_rates()
    
    def setup_ui(self):
        # Main title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        title_frame.pack(fill='x') 
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="Professional Currency Converter", 
                              font=('Arial', 24, 'bold'), fg='white', bg='#2c3e50')
        title_label.pack(expand=True)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=40, pady=30)
        main_frame.pack(fill='both', expand=True)
        
        # From currency section
        from_frame = tk.Frame(main_frame, bg='#ffffff', relief='raised', bd=2, padx=20, pady=15)
        from_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(from_frame, text="From Currency:", font=('Arial', 12, 'bold'), 
                bg='#ffffff').pack(anchor='w')
        
        self.from_currency = ttk.Combobox(from_frame, values=list(self.currencies.keys()),
                                         font=('Arial', 11), width=15, state='readonly')
        self.from_currency.set('USD')
        self.from_currency.pack(pady=(5, 10), anchor='w')
        
        self.amount_entry = tk.Entry(from_frame, font=('Arial', 12), width=20, 
                                   relief='solid', bd=1)
        self.amount_entry.pack(anchor='w')
        self.amount_entry.insert(0, '1.00')
        
        # To currency section
        to_frame = tk.Frame(main_frame, bg='#ffffff', relief='raised', bd=2, padx=20, pady=15)
        to_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(to_frame, text="To Currency:", font=('Arial', 12, 'bold'), 
                bg='#ffffff').pack(anchor='w')
        
        self.to_currency = ttk.Combobox(to_frame, values=list(self.currencies.keys()),
                                       font=('Arial', 11), width=15, state='readonly')
        self.to_currency.set('EUR')
        self.to_currency.pack(pady=(5, 10), anchor='w')
        
        self.result_label = tk.Label(to_frame, text="0.00", font=('Arial', 16, 'bold'),
                                   bg='#ffffff', fg='#2c3e50')
        self.result_label.pack(anchor='w')
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill='x', pady=20)
        
        convert_btn = tk.Button(button_frame, text="Convert", command=self.convert_currency,
                               bg='#3498db', fg='white', font=('Arial', 12, 'bold'),
                               relief='flat', padx=30, pady=8, cursor='hand2')
        convert_btn.pack(side='left', padx=(0, 10))
        
        refresh_btn = tk.Button(button_frame, text="Refresh Rates", command=self.update_rates,
                               bg='#27ae60', fg='white', font=('Arial', 12, 'bold'),
                               relief='flat', padx=30, pady=8, cursor='hand2')
        refresh_btn.pack(side='left', padx=(0, 10))
        
        swap_btn = tk.Button(button_frame, text="Swap", command=self.swap_currencies,
                            bg='#e67e22', fg='white', font=('Arial', 12, 'bold'),
                            relief='flat', padx=30, pady=8, cursor='hand2')
        swap_btn.pack(side='left')
        
        # Status frame
        status_frame = tk.Frame(main_frame, bg='#ecf0f1', relief='sunken', bd=1, padx=20, pady=10)
        status_frame.pack(fill='x', pady=(20, 0))
        
        self.status_label = tk.Label(status_frame, text="Loading exchange rates...", 
                                   font=('Arial', 10), bg='#ecf0f1', fg='#7f8c8d')
        self.status_label.pack(anchor='w')
        
        self.rate_info_label = tk.Label(status_frame, text="", font=('Arial', 10, 'italic'), 
                                      bg='#ecf0f1', fg='#34495e')
        self.rate_info_label.pack(anchor='w')
        
        # Bind events
        self.amount_entry.bind('<KeyRelease>', lambda e: self.convert_currency())
        self.from_currency.bind('<<ComboboxSelected>>', lambda e: self.convert_currency())
        self.to_currency.bind('<<ComboboxSelected>>', lambda e: self.convert_currency())
    
    def update_rates(self):
        def fetch_rates():
            try:
                # Using exchangerate-api.com (free tier allows 1500 requests/month)
                response = requests.get('https://api.exchangerate-api.com/v4/latest/USD', timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    self.exchange_rates = data['rates']
                    self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    self.root.after(0, self.update_status_success)
                else:
                    self.root.after(0, self.update_status_error)
            except Exception as e:
                
                
                
                self.root.after(0, lambda: self.update_status_error(str(e)))
        
        # Run in separate thread to prevent UI freezing
        threading.Thread(target=fetch_rates, daemon=True).start()
        self.status_label.config(text="Updating exchange rates...")
    
    def update_status_success(self):
        self.status_label.config(text=f"Exchange rates updated successfully at {self.last_update}")
        self.convert_currency()
    
    def update_status_error(self, error_msg="Failed to fetch exchange rates"):
        self.status_label.config(text=f"Error: {error_msg}")
        messagebox.showwarning("Connection Error", 
                             "Unable to fetch live exchange rates. Please check your internet connection.")
    
    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get().replace(',', ''))
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            if not self.exchange_rates:
                self.result_label.config(text="No exchange data available")
                return
            
            # Convert from source currency to USD, then to target currency
            if from_curr == 'USD':
                usd_amount = amount
            else:
                usd_amount = amount / self.exchange_rates.get(from_curr, 1)
            
            if to_curr == 'USD':
                result = usd_amount
            else:
                result = usd_amount * self.exchange_rates.get(to_curr, 1)
            
            # Format result with proper currency symbol and formatting
            formatted_result = f"{result:,.4f}"
            self.result_label.config(text=f"{formatted_result} {to_curr}")
            
            # Update rate info
            if from_curr != to_curr:
                rate = result / amount if amount != 0 else 0
                self.rate_info_label.config(text=f"1 {from_curr} = {rate:.4f} {to_curr}")
            else:
                self.rate_info_label.config(text="")
                
        except ValueError:
            self.result_label.config(text="Invalid amount")
            self.rate_info_label.config(text="")
        except Exception as e:
            self.result_label.config(text="Conversion error")
            self.rate_info_label.config(text="")
    
    def swap_currencies(self):
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        
        self.from_currency.set(to_curr)
        self.to_currency.set(from_curr)
        
        self.convert_currency()
    
    def run(self):
        self.root.mainloop()

# Create and run the application
if __name__ == "__main__":
    app = CurrencyConverter()
    app.run()