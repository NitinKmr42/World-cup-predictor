# Team to Confederation Mapping
# Based on FIFA confederation membership + historical/dissolved nations
# Check against your dataset's team names: pd.unique(df[['home_team', 'away_team']].values.ravel())
# Correct any mismatches you find

team_to_confederation = {

    # =========================================================
    # UEFA - Europe
    # =========================================================
    "Albania": "UEFA",
    "Andorra": "UEFA",
    "Armenia": "UEFA",
    "Austria": "UEFA",
    "Azerbaijan": "UEFA",
    "Belarus": "UEFA",
    "Belgium": "UEFA",
    "Bosnia and Herzegovina": "UEFA",
    "Bosnia-Herzegovina": "UEFA",
    "Bulgaria": "UEFA",
    "Croatia": "UEFA",
    "Cyprus": "UEFA",
    "Czech Republic": "UEFA",
    "Czechia": "UEFA",
    "Denmark": "UEFA",
    "England": "UEFA",
    "Estonia": "UEFA",
    "Faroe Islands": "UEFA",
    "Finland": "UEFA",
    "France": "UEFA",
    "Georgia": "UEFA",
    "Germany": "UEFA",
    "Gibraltar": "UEFA",
    "Greece": "UEFA",
    "Hungary": "UEFA",
    "Iceland": "UEFA",
    "Israel": "UEFA",
    "Italy": "UEFA",
    "Kazakhstan": "UEFA",
    "Kosovo": "UEFA",
    "Latvia": "UEFA",
    "Liechtenstein": "UEFA",
    "Lithuania": "UEFA",
    "Luxembourg": "UEFA",
    "Malta": "UEFA",
    "Moldova": "UEFA",
    "Monaco": "UEFA",
    "Montenegro": "UEFA",
    "Netherlands": "UEFA",
    "North Macedonia": "UEFA",
    "Northern Ireland": "UEFA",
    "Norway": "UEFA",
    "Poland": "UEFA",
    "Portugal": "UEFA",
    "Republic of Ireland": "UEFA",
    "Romania": "UEFA",
    "Russia": "UEFA",
    "San Marino": "UEFA",
    "Scotland": "UEFA",
    "Serbia": "UEFA",
    "Slovakia": "UEFA",
    "Slovenia": "UEFA",
    "Spain": "UEFA",
    "Sweden": "UEFA",
    "Switzerland": "UEFA",
    "Turkey": "UEFA",
    "Ukraine": "UEFA",
    "Wales": "UEFA",

    # Historical UEFA nations
    "West Germany": "UEFA",
    "East Germany": "UEFA",
    "Soviet Union": "UEFA",
    "Yugoslavia": "UEFA",
    "Czechoslovakia": "UEFA",
    "Serbia and Montenegro": "UEFA",
    "Federal Republic of Yugoslavia": "UEFA",
    "Kingdom of Yugoslavia": "UEFA",

    # =========================================================
    # CONMEBOL - South America
    # =========================================================
    "Argentina": "CONMEBOL",
    "Bolivia": "CONMEBOL",
    "Brazil": "CONMEBOL",
    "Chile": "CONMEBOL",
    "Colombia": "CONMEBOL",
    "Ecuador": "CONMEBOL",
    "Paraguay": "CONMEBOL",
    "Peru": "CONMEBOL",
    "Uruguay": "CONMEBOL",
    "Venezuela": "CONMEBOL",

    # =========================================================
    # CONCACAF - North/Central America & Caribbean
    # =========================================================
    "Anguilla": "CONCACAF",
    "Antigua and Barbuda": "CONCACAF",
    "Aruba": "CONCACAF",
    "Bahamas": "CONCACAF",
    "Barbados": "CONCACAF",
    "Belize": "CONCACAF",
    "Bermuda": "CONCACAF",
    "British Virgin Islands": "CONCACAF",
    "Canada": "CONCACAF",
    "Cayman Islands": "CONCACAF",
    "Costa Rica": "CONCACAF",
    "Cuba": "CONCACAF",
    "Dominica": "CONCACAF",
    "Dominican Republic": "CONCACAF",
    "El Salvador": "CONCACAF",
    "French Guiana": "CONCACAF",
    "Grenada": "CONCACAF",
    "Guadeloupe": "CONCACAF",
    "Guatemala": "CONCACAF",
    "Guyana": "CONCACAF",
    "Haiti": "CONCACAF",
    "Honduras": "CONCACAF",
    "Jamaica": "CONCACAF",
    "Martinique": "CONCACAF",
    "Mexico": "CONCACAF",
    "Montserrat": "CONCACAF",
    "Nicaragua": "CONCACAF",
    "Panama": "CONCACAF",
    "Puerto Rico": "CONCACAF",
    "Saint Kitts and Nevis": "CONCACAF",
    "Saint Lucia": "CONCACAF",
    "Saint Vincent and the Grenadines": "CONCACAF",
    "Sint Maarten": "CONCACAF",
    "Suriname": "CONCACAF",
    "Trinidad and Tobago": "CONCACAF",
    "Turks and Caicos Islands": "CONCACAF",
    "United States": "CONCACAF",
    "US Virgin Islands": "CONCACAF",

    # Historical CONCACAF
    "United States Virgin Islands": "CONCACAF",
    "Netherlands Antilles": "CONCACAF",

    # =========================================================
    # CAF - Africa
    # =========================================================
    "Algeria": "CAF",
    "Angola": "CAF",
    "Benin": "CAF",
    "Botswana": "CAF",
    "Burkina Faso": "CAF",
    "Burundi": "CAF",
    "Cameroon": "CAF",
    "Cape Verde": "CAF",
    "Central African Republic": "CAF",
    "Chad": "CAF",
    "Comoros": "CAF",
    "Congo": "CAF",
    "DR Congo": "CAF",
    "Djibouti": "CAF",
    "Egypt": "CAF",
    "Equatorial Guinea": "CAF",
    "Eritrea": "CAF",
    "Eswatini": "CAF",
    "Ethiopia": "CAF",
    "Gabon": "CAF",
    "Gambia": "CAF",
    "Ghana": "CAF",
    "Guinea": "CAF",
    "Guinea-Bissau": "CAF",
    "Ivory Coast": "CAF",
    "Kenya": "CAF",
    "Lesotho": "CAF",
    "Liberia": "CAF",
    "Libya": "CAF",
    "Madagascar": "CAF",
    "Malawi": "CAF",
    "Mali": "CAF",
    "Mauritania": "CAF",
    "Mauritius": "CAF",
    "Morocco": "CAF",
    "Mozambique": "CAF",
    "Namibia": "CAF",
    "Niger": "CAF",
    "Nigeria": "CAF",
    "Rwanda": "CAF",
    "São Tomé and Príncipe": "CAF",
    "Senegal": "CAF",
    "Seychelles": "CAF",
    "Sierra Leone": "CAF",
    "Somalia": "CAF",
    "South Africa": "CAF",
    "South Sudan": "CAF",
    "Sudan": "CAF",
    "Swaziland": "CAF",
    "Tanzania": "CAF",
    "Togo": "CAF",
    "Tunisia": "CAF",
    "Uganda": "CAF",
    "Zambia": "CAF",
    "Zimbabwe": "CAF",

    # Historical CAF
    "Zaire": "CAF",
    "Rhodesia": "CAF",

    # =========================================================
    # AFC - Asia
    # =========================================================
    "Afghanistan": "AFC",
    "Australia": "AFC",  # moved from OFC to AFC in 2006
    "Bahrain": "AFC",
    "Bangladesh": "AFC",
    "Bhutan": "AFC",
    "Brunei": "AFC",
    "Cambodia": "AFC",
    "China": "AFC",
    "China PR": "AFC",
    "Chinese Taipei": "AFC",
    "Guam": "AFC",
    "Hong Kong": "AFC",
    "India": "AFC",
    "Indonesia": "AFC",
    "Iran": "AFC",
    "Iraq": "AFC",
    "Japan": "AFC",
    "Jordan": "AFC",
    "Kuwait": "AFC",
    "Kyrgyzstan": "AFC",
    "Laos": "AFC",
    "Lebanon": "AFC",
    "Macau": "AFC",
    "Malaysia": "AFC",
    "Maldives": "AFC",
    "Mongolia": "AFC",
    "Myanmar": "AFC",
    "Nepal": "AFC",
    "North Korea": "AFC",
    "Northern Mariana Islands": "AFC",
    "Oman": "AFC",
    "Pakistan": "AFC",
    "Palestine": "AFC",
    "Philippines": "AFC",
    "Qatar": "AFC",
    "Saudi Arabia": "AFC",
    "Singapore": "AFC",
    "South Korea": "AFC",
    "Sri Lanka": "AFC",
    "Syria": "AFC",
    "Tajikistan": "AFC",
    "Thailand": "AFC",
    "Timor-Leste": "AFC",
    "Turkmenistan": "AFC",
    "United Arab Emirates": "AFC",
    "Uzbekistan": "AFC",
    "Vietnam": "AFC",
    "Yemen": "AFC",

    # Historical AFC
    "South Vietnam": "AFC",
    "North Vietnam": "AFC",
    "South Yemen": "AFC",

    # =========================================================
    # OFC - Oceania
    # =========================================================
    "American Samoa": "OFC",
    "Cook Islands": "OFC",
    "Fiji": "OFC",
    "Kiribati": "OFC",
    "Marshall Islands": "OFC",
    "Micronesia": "OFC",
    "Nauru": "OFC",
    "New Caledonia": "OFC",
    "New Zealand": "OFC",
    "Niue": "OFC",
    "Papua New Guinea": "OFC",
    "Samoa": "OFC",
    "Solomon Islands": "OFC",
    "Tahiti": "OFC",
    "Tonga": "OFC",
    "Tuvalu": "OFC",
    "Vanuatu": "OFC",

    # Historical OFC (before AFC move)
    "Australia (OFC)": "OFC",
}

def get_confederation(team):
    return team_to_confederation.get(team, "Unknown")# Team to Confederation Mapping
# Based on FIFA confederation membership + historical/dissolved nations
# Check against your dataset's team names: pd.unique(df[['home_team', 'away_team']].values.ravel())
# Correct any mismatches you find

team_to_confederation = {

    # =========================================================
    # UEFA - Europe
    # =========================================================
    "Albania": "UEFA",
    "Andorra": "UEFA",
    "Armenia": "UEFA",
    "Austria": "UEFA",
    "Azerbaijan": "UEFA",
    "Belarus": "UEFA",
    "Belgium": "UEFA",
    "Bosnia and Herzegovina": "UEFA",
    "Bosnia-Herzegovina": "UEFA",
    "Bulgaria": "UEFA",
    "Croatia": "UEFA",
    "Cyprus": "UEFA",
    "Czech Republic": "UEFA",
    "Czechia": "UEFA",
    "Denmark": "UEFA",
    "England": "UEFA",
    "Estonia": "UEFA",
    "Faroe Islands": "UEFA",
    "Finland": "UEFA",
    "France": "UEFA",
    "Georgia": "UEFA",
    "Germany": "UEFA",
    "Gibraltar": "UEFA",
    "Greece": "UEFA",
    "Hungary": "UEFA",
    "Iceland": "UEFA",
    "Israel": "UEFA",
    "Italy": "UEFA",
    "Kazakhstan": "UEFA",
    "Kosovo": "UEFA",
    "Latvia": "UEFA",
    "Liechtenstein": "UEFA",
    "Lithuania": "UEFA",
    "Luxembourg": "UEFA",
    "Malta": "UEFA",
    "Moldova": "UEFA",
    "Monaco": "UEFA",
    "Montenegro": "UEFA",
    "Netherlands": "UEFA",
    "North Macedonia": "UEFA",
    "Northern Ireland": "UEFA",
    "Norway": "UEFA",
    "Poland": "UEFA",
    "Portugal": "UEFA",
    "Republic of Ireland": "UEFA",
    "Romania": "UEFA",
    "Russia": "UEFA",
    "San Marino": "UEFA",
    "Scotland": "UEFA",
    "Serbia": "UEFA",
    "Slovakia": "UEFA",
    "Slovenia": "UEFA",
    "Spain": "UEFA",
    "Sweden": "UEFA",
    "Switzerland": "UEFA",
    "Turkey": "UEFA",
    "Ukraine": "UEFA",
    "Wales": "UEFA",

    # Historical UEFA nations
    "West Germany": "UEFA",
    "East Germany": "UEFA",
    "Soviet Union": "UEFA",
    "Yugoslavia": "UEFA",
    "Czechoslovakia": "UEFA",
    "Serbia and Montenegro": "UEFA",
    "Federal Republic of Yugoslavia": "UEFA",
    "Kingdom of Yugoslavia": "UEFA",

    # =========================================================
    # CONMEBOL - South America
    # =========================================================
    "Argentina": "CONMEBOL",
    "Bolivia": "CONMEBOL",
    "Brazil": "CONMEBOL",
    "Chile": "CONMEBOL",
    "Colombia": "CONMEBOL",
    "Ecuador": "CONMEBOL",
    "Paraguay": "CONMEBOL",
    "Peru": "CONMEBOL",
    "Uruguay": "CONMEBOL",
    "Venezuela": "CONMEBOL",

    # =========================================================
    # CONCACAF - North/Central America & Caribbean
    # =========================================================
    "Anguilla": "CONCACAF",
    "Antigua and Barbuda": "CONCACAF",
    "Aruba": "CONCACAF",
    "Bahamas": "CONCACAF",
    "Barbados": "CONCACAF",
    "Belize": "CONCACAF",
    "Bermuda": "CONCACAF",
    "British Virgin Islands": "CONCACAF",
    "Canada": "CONCACAF",
    "Cayman Islands": "CONCACAF",
    "Costa Rica": "CONCACAF",
    "Cuba": "CONCACAF",
    "Dominica": "CONCACAF",
    "Dominican Republic": "CONCACAF",
    "El Salvador": "CONCACAF",
    "French Guiana": "CONCACAF",
    "Grenada": "CONCACAF",
    "Guadeloupe": "CONCACAF",
    "Guatemala": "CONCACAF",
    "Guyana": "CONCACAF",
    "Haiti": "CONCACAF",
    "Honduras": "CONCACAF",
    "Jamaica": "CONCACAF",
    "Martinique": "CONCACAF",
    "Mexico": "CONCACAF",
    "Montserrat": "CONCACAF",
    "Nicaragua": "CONCACAF",
    "Panama": "CONCACAF",
    "Puerto Rico": "CONCACAF",
    "Saint Kitts and Nevis": "CONCACAF",
    "Saint Lucia": "CONCACAF",
    "Saint Vincent and the Grenadines": "CONCACAF",
    "Sint Maarten": "CONCACAF",
    "Suriname": "CONCACAF",
    "Trinidad and Tobago": "CONCACAF",
    "Turks and Caicos Islands": "CONCACAF",
    "United States": "CONCACAF",
    "US Virgin Islands": "CONCACAF",

    # Historical CONCACAF
    "United States Virgin Islands": "CONCACAF",
    "Netherlands Antilles": "CONCACAF",

    # =========================================================
    # CAF - Africa
    # =========================================================
    "Algeria": "CAF",
    "Angola": "CAF",
    "Benin": "CAF",
    "Botswana": "CAF",
    "Burkina Faso": "CAF",
    "Burundi": "CAF",
    "Cameroon": "CAF",
    "Cape Verde": "CAF",
    "Central African Republic": "CAF",
    "Chad": "CAF",
    "Comoros": "CAF",
    "Congo": "CAF",
    "DR Congo": "CAF",
    "Djibouti": "CAF",
    "Egypt": "CAF",
    "Equatorial Guinea": "CAF",
    "Eritrea": "CAF",
    "Eswatini": "CAF",
    "Ethiopia": "CAF",
    "Gabon": "CAF",
    "Gambia": "CAF",
    "Ghana": "CAF",
    "Guinea": "CAF",
    "Guinea-Bissau": "CAF",
    "Ivory Coast": "CAF",
    "Kenya": "CAF",
    "Lesotho": "CAF",
    "Liberia": "CAF",
    "Libya": "CAF",
    "Madagascar": "CAF",
    "Malawi": "CAF",
    "Mali": "CAF",
    "Mauritania": "CAF",
    "Mauritius": "CAF",
    "Morocco": "CAF",
    "Mozambique": "CAF",
    "Namibia": "CAF",
    "Niger": "CAF",
    "Nigeria": "CAF",
    "Rwanda": "CAF",
    "São Tomé and Príncipe": "CAF",
    "Senegal": "CAF",
    "Seychelles": "CAF",
    "Sierra Leone": "CAF",
    "Somalia": "CAF",
    "South Africa": "CAF",
    "South Sudan": "CAF",
    "Sudan": "CAF",
    "Swaziland": "CAF",
    "Tanzania": "CAF",
    "Togo": "CAF",
    "Tunisia": "CAF",
    "Uganda": "CAF",
    "Zambia": "CAF",
    "Zimbabwe": "CAF",

    # Historical CAF
    "Zaire": "CAF",
    "Rhodesia": "CAF",

    # =========================================================
    # AFC - Asia
    # =========================================================
    "Afghanistan": "AFC",
    "Australia": "AFC",  # moved from OFC to AFC in 2006
    "Bahrain": "AFC",
    "Bangladesh": "AFC",
    "Bhutan": "AFC",
    "Brunei": "AFC",
    "Cambodia": "AFC",
    "China": "AFC",
    "China PR": "AFC",
    "Chinese Taipei": "AFC",
    "Guam": "AFC",
    "Hong Kong": "AFC",
    "India": "AFC",
    "Indonesia": "AFC",
    "Iran": "AFC",
    "Iraq": "AFC",
    "Japan": "AFC",
    "Jordan": "AFC",
    "Kuwait": "AFC",
    "Kyrgyzstan": "AFC",
    "Laos": "AFC",
    "Lebanon": "AFC",
    "Macau": "AFC",
    "Malaysia": "AFC",
    "Maldives": "AFC",
    "Mongolia": "AFC",
    "Myanmar": "AFC",
    "Nepal": "AFC",
    "North Korea": "AFC",
    "Northern Mariana Islands": "AFC",
    "Oman": "AFC",
    "Pakistan": "AFC",
    "Palestine": "AFC",
    "Philippines": "AFC",
    "Qatar": "AFC",
    "Saudi Arabia": "AFC",
    "Singapore": "AFC",
    "South Korea": "AFC",
    "Sri Lanka": "AFC",
    "Syria": "AFC",
    "Tajikistan": "AFC",
    "Thailand": "AFC",
    "Timor-Leste": "AFC",
    "Turkmenistan": "AFC",
    "United Arab Emirates": "AFC",
    "Uzbekistan": "AFC",
    "Vietnam": "AFC",
    "Yemen": "AFC",

    # Historical AFC
    "South Vietnam": "AFC",
    "North Vietnam": "AFC",
    "South Yemen": "AFC",

    # =========================================================
    # OFC - Oceania
    # =========================================================
    "American Samoa": "OFC",
    "Cook Islands": "OFC",
    "Fiji": "OFC",
    "Kiribati": "OFC",
    "Marshall Islands": "OFC",
    "Micronesia": "OFC",
    "Nauru": "OFC",
    "New Caledonia": "OFC",
    "New Zealand": "OFC",
    "Niue": "OFC",
    "Papua New Guinea": "OFC",
    "Samoa": "OFC",
    "Solomon Islands": "OFC",
    "Tahiti": "OFC",
    "Tonga": "OFC",
    "Tuvalu": "OFC",
    "Vanuatu": "OFC",

    # Historical OFC (before AFC move)
    "Australia (OFC)": "OFC",
    
    # Historical and colonial era teams
    "Aden": "AFC",                        # Yemen
    "Belgian Congo": "CAF",               # DR Congo
    "Bohemia": "UEFA",                    # Czech Republic
    "Bohemia and Moravia": "UEFA",        # Czech Republic
    "Bonaire": "CONCACAF",
    "British Guiana": "CONCACAF",         # Guyana
    "British Honduras": "CONCACAF",       # Belize
    "British India": "AFC",               # India
    "Burma": "AFC",                       # Myanmar
    "Ceylon": "AFC",                      # Sri Lanka
    "Chagos Islands": "AFC",
    "Comm of Indep States": "UEFA",       # post-Soviet union transitional team
    "Congo-Leopoldville": "CAF",          # DR Congo
    "Curaçao": "CONCACAF",
    "Dahomey": "CAF",                     # Benin
    "Dutch East Indies": "AFC",           # Indonesia
    "East Timor": "AFC",                  # Timor-Leste
    "Eastern Samoa": "OFC",               # American Samoa
    "FS Micronesia": "OFC",
    "Falkland Islands": "CONMEBOL",
    "French Congo": "CAF",                # Congo
    "French Dahomey": "CAF",              # Benin
    "French Somaliland": "CAF",           # Djibouti
    "French Sudan": "CAF",                # Mali
    "French Togoland": "CAF",             # Togo
    "Gold Coast": "CAF",                  # Ghana
    "Greenland": "UEFA",
    "Ireland": "UEFA",                    # pre-partition Ireland
    "Khmer Republic": "AFC",              # Cambodia
    "Korea": "AFC",                       # pre-division Korea
    "Kurdistan": "AFC",
    "Macao": "AFC",                       # Macau variant
    "Macedonia": "UEFA",                  # North Macedonia
    "Malaya": "AFC",                      # Malaysia
    "Mali Federation": "CAF",
    "Mayotte": "CAF",
    "New Hebrides": "OFC",                # Vanuatu
    "North Yemen": "AFC",
    "Northern Cyprus": "UEFA",
    "Northern Rhodesia": "CAF",           # Zambia
    "Nyasaland": "CAF",                   # Malawi
    "Palau": "OFC",
    "Portuguese Guinea": "CAF",           # Guinea-Bissau
    "Reunion": "CAF",
    "Ruanda-Urundi": "CAF",               # Rwanda/Burundi
    "Saar": "UEFA",                       # historical German territory
    "Saint Barthelemy": "CONCACAF",
    "Saint Kitts": "CONCACAF",
    "Saint Martin": "CONCACAF",
    "Saint Pierre and Miquelon": "CONCACAF",
    "Sao Tome and Principe": "CAF",       # name variant
    "Sint Eustatius": "CONCACAF",
    "Southern Rhodesia": "CAF",           # Zimbabwe
    "St Vincent & Grenadines": "CONCACAF", # name variant
    "Taiwan": "AFC",                      # Chinese Taipei variant
    "Tanganyika": "CAF",                  # Tanzania
    "Tibet": "AFC",
    "Ubangi-Shari": "CAF",               # Central African Republic
    "United Arab Republic": "CAF",        # Egypt/Syria union 1958-61
    "Upper Volta": "CAF",                 # Burkina Faso
    "Wallis and Futuna": "OFC",
    "Western Samoa": "OFC",               # Samoa
    "Zanzibar": "CAF",                    # Tanzania
    "São Tome and Principe": "CAF",
}

def get_confederation(team):
    return team_to_confederation.get(team, "Unknown")