from flask import Flask, jsonify, send_from_directory
app = Flask(__name__, static_url_path='', static_folder='.')

firstAidData = {
  "Acute Poisoning": {
    "steps": [
      "<b>Provide First Aid:</b> While waiting for emergency responders to arrive, if it's safe to do so, provide first aid as needed.",
      "<b>Move the affected person:</b> to a well-ventilated area if exposed to toxic fumes.",
      "<b>Remove contaminated clothing:</b>",
      "<b>Ingestion precautions:</b> If the poison is ingested, do not induce vomiting unless instructed by medical professionals."
    ],
    "medicine": [
      "<b>Activated Charcoal:</b> Used to absorb toxins in the gastrointestinal tract and prevent their absorption into the bloodstream.",
      "<b>Antidotes:</b> Some poisons have specific antidotes that can counteract their effects. For example, naloxone is used for opioid overdose, while atropine or pralidoxime are used for certain pesticide poisonings.",
      "<b>Supportive Care:</b> Measures to maintain vital functions, including IV fluids, oxygen therapy, and monitoring vital signs.",
      "<b>Gastric Lavage:</b> Performed in some cases to remove toxins from the stomach.",
      "<b>Medications:</b> Depending on symptoms and type of poisoning, medications may be given to manage nausea, seizures, or respiratory distress.",
      "<b>Dialysis:</b> Used if toxins cause kidney damage or are not eliminated effectively."
    ],
"emergency": "\n  <b>If the person is unconscious, vomiting continuously, or having trouble breathing—seek emergency help immediately.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/acute.jpg"
  },
  "Allergic Reactions": {
    "steps": [
      "<b>Identify and Remove the Allergen:</b> Stop exposure immediately.",
      "<b>Take Antihistamines:</b> Follow dosage instructions as advised.",
      "<b>Apply Topical Creams for Skin Reactions:</b> Use steroids like hydrocortisone as directed.",
      "<b>Monitor Symptoms:</b> Watch for worsening conditions."
    ],
    "medicine": [
      {
        "name": "<b>Antihistamines</b>",
        "purpose": "Reduce sneezing, itching, nasal congestion, and hives.",
        "examples": "Cetirizine (Zyrtec), Loratadine (Claritin), Fexofenadine (Allegra), Diphenhydramine (Benadryl)"
      },
      {
        "name": "<b>Nasal Corticosteroids</b>",
        "purpose": "Relieve inflammation and symptoms such as nasal congestion, sneezing, and runny nose.",
        "examples": "Fluticasone (Flonase), Budesonide (Rhinocort), Mometasone (Nasonex)"
      },
      {
        "name": "<b>Decongestants</b>",
        "purpose": "Relieve nasal congestion (short-term use recommended).",
        "examples": "Pseudoephedrine (Sudafed), Phenylephrine"
      },
      {
        "name": "<b>Leukotriene Receptor Antagonists</b>",
        "purpose": "Block leukotrienes to reduce allergic symptoms.",
        "examples": "Montelukast (Singulair)"
      },
      {
        "name": "<b>Mast Cell Stabilizers</b>",
        "purpose": "Prevent release of histamine and other chemicals from mast cells.",
        "examples": "Cromolyn sodium (NasalCrom)"
      },
      {
        "name": "<b>Topical Treatments for Skin Allergies</b>",
        "purpose": "Relieve skin itching, redness, and swelling.",
        "examples": "Hydrocortisone cream, Calamine lotion"
      }
    ],
"emergency": "\n  <b>If symptoms include difficulty breathing, swelling of the face or throat, or signs of anaphylaxis—call emergency services at once.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/allergy.jpg"
  },
  "Animal Bites": {
    "steps": [
      "<b>Wash the Wound:</b> Rinse with mild soap and running water for at least 5 minutes.",
      "<b>Control Bleeding:</b> Apply gentle pressure with a clean cloth or sterile gauze; elevate if possible.",
      "<b>Apply Antiseptic:</b> Apply antiseptic solution or antibiotic ointment.",
      "<b>Cover the Wound:</b> Use a clean, sterile bandage; change regularly.",
      "<b>Monitor for Signs of Infection:</b> Watch for pain, redness, swelling, warmth, or pus; seek care if noticed."
    ],
    "medicine": [
      {
        "name": "<b>Tetanus Vaccine</b>",
        "purpose": "Prevent tetanus infection in deep or contaminated bites.",
        "examples": "Booster may be needed if last vaccination was >5–10 years ago"
      },
      {
        "name": "<b>Rabies Vaccine</b>",
        "purpose": "Prevent rabies infection after suspected rabid animal bite.",
        "examples": "Series of rabies vaccinations depending on risk"
      },
      {
        "name": "<b>Rabies Immune Globulin (RIG)</b>",
        "purpose": "Provides immediate protection against rabies.",
        "examples": "Administered for high-risk bites"
      },
      {
        "name": "<b>Antibiotics</b>",
        "purpose": "Prevent or treat bacterial infections from the bite.",
        "examples": "Prescribed for deep puncture wounds, hand/face bites, or high-risk animals"
      },
      {
        "name": "<b>Pain Medication</b>",
        "purpose": "Relieve pain and discomfort.",
        "examples": "Acetaminophen (Tylenol), Ibuprofen (Advil, Motrin)"
      },
      {
        "name": "<b>Tetanus Toxoid</b>",
        "purpose": "Additional tetanus protection if vaccination history is unclear.",
        "examples": "Administered as needed"
      }
    ],
"emergency": "\n  <b>If the bite is deep, bleeding severely, or from a suspected rabid animal—seek urgent medical care.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/animal_bite.jpg"
  },
  "Asthma Attack": {
    "steps": [
      "<b>Stay Calm:</b> Panic can worsen breathing; sit upright and relax shoulders.",
      "<b>Use Your Quick-Relief Inhaler:</b> Short-acting beta agonist (SABA) like albuterol; follow your asthma action plan.",
      "<b>Follow the 20-Minute Rule:</b> If symptoms don’t improve after initial puffs, follow action plan instructions.",
      "<b>Seek Emergency Care if Necessary:</b> Difficulty breathing, cannot speak full sentences, throat tightening, or blue lips/fingernails requires immediate attention."
    ],
    "medicine": [
      {
        "name": "<b>Short-acting Beta Agonists (SABA)</b>",
        "purpose": "Quickly relax and open the airways for rapid relief.",
        "examples": "Albuterol (Ventolin, ProAir, Proventil), Levalbuterol (Xopenex)",
        "form": "Inhaler or nebulized solution"
      },
      {
        "name": "<b>Ipratropium Bromide (Atrovent)</b>",
        "purpose": "Bronchodilator that relaxes airway muscles.",
        "form": "Inhaler or nebulized solution",
        "note": "Often used with SABAs in severe attacks"
      },
      {
        "name": "<b>Oral Corticosteroids</b>",
        "purpose": "Reduce airway inflammation and swelling.",
        "examples": "Prednisone, Prednisolone",
        "form": "Tablets or liquid"
      },
      {
        "name": "<b>Magnesium Sulfate</b>",
        "purpose": "Acts as bronchodilator in severe attacks.",
        "form": "IV administration in hospital"
      },
      {
        "name": "<b>Epinephrine (Adrenaline)</b>",
        "purpose": "Used in life-threatening asthma or anaphylaxis to open airways.",
        "form": "Intramuscular or subcutaneous injection by healthcare professionals"
      },
      {
        "name": "<b>Systemic Beta Agonists</b>",
        "purpose": "Similar to SABAs but given orally or IV in severe cases.",
        "examples": "Terbutaline (Brethine)"
      },
      {
        "name": "<b>Oxygen Therapy</b>",
        "purpose": "Supplemental oxygen for adequate oxygenation in severe attacks."
      }
    ],
"emergency": "\n  <b>If there is severe difficulty breathing, blue lips, or the inhaler is not helping—seek emergency assistance immediately.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/asthma.jpg"
  },
  "Bleeding": {
    "steps": [
      "<b>Assess the Situation:</b> Determine whether bleeding is minor or severe. Severe bleeding requires immediate medical attention.",
      "<b>Protect Yourself:</b> Wear gloves or use a barrier to avoid exposure to bloodborne pathogens.",
      "<b>Apply Direct Pressure:</b> Use a clean cloth, sterile gauze, or clothing. Add layers if soaked, do not remove soaked cloth.",
      "<b>Elevate the Injured Area:</b> Raise the wounded area above the heart if possible.",
      "<b>Maintain Pressure:</b> Keep pressure until bleeding stops or medical help arrives.",
      "<b>Apply Pressure Points:</b> If direct pressure fails, press on major arteries near the wound: brachial, femoral, radial, carotid.",
      "<b>Use Tourniquet (if necessary):</b> Apply 2-3 inches above wound, note time applied, inform medical personnel immediately."
    ],
    "medicine": [
      "<b>Topical Hemostatic Agents:</b> Promote clotting and stop bleeding.",
      "<b>Antiseptic Powder:</b> Contains hemostatic agents like aluminum sulfate or ferric subsulfate.",
      "<b>Topical Thrombin:</b> Protein applied directly to bleeding wounds to aid clot formation.",
      "<b>Tranexamic Acid (TXA):</b> Prevents excessive bleeding by inhibiting clot breakdown.",
      "<b>Desmopressin (DDAVP):</b> Promotes release of von Willebrand factor and factor VIII.",
      "<b>Factor Replacement Therapy:</b> Clotting factor concentrates for hemophilia or congenital bleeding disorders.",
      "<b>Platelet Transfusion:</b> For severe thrombocytopenia or platelet dysfunction.",
      "<b>Prothrombin Complex Concentrate (PCC):</b> Contains factors II, VII, IX, and X for clotting.",
      "<b>Fibrinolytic Inhibitors:</b> Aminocaproic acid or tranexamic acid to stabilize blood clots."
    ],
"emergency": "\n  <b>If bleeding does not stop after 10 minutes of pressure, or blood is spurting—call emergency help right away.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/bleeding.jpg"
  },
  "Burns": {
    "steps": [
      "<b>Stop the Burning Process:</b> Remove person from flames or hot liquids. Stop, drop, and roll if clothing is on fire.",
      "<b>Cool the Burn:</b> Hold under cool running water 10-20 minutes. Avoid ice or ice water.",
      "<b>Remove Clothing and Jewelry:</b> Remove carefully unless stuck to the skin.",
      "<b>Cover the Burn:</b> Use sterile, non-adhesive bandage or clean cloth.",
      "<b>Do Not Break Blisters:</b> Blisters protect the skin and aid healing.",
      "<b>Monitor for Signs of Infection:</b> Redness, swelling, warmth, pus indicate infection."
    ],
    "medicine": [
      "<b>Topical Antibacterial Agents:</b> Silver sulfadiazine cream, Mafenide acetate cream.",
      "<b>Pain Management:</b> NSAIDs (Ibuprofen, Naproxen), Acetaminophen (Tylenol).",
      "<b>Prescription Pain Medications:</b> Stronger opioids like morphine or oxycodone for severe burns.",
      "<b>Antibiotics:</b> Oral or IV antibiotics if infection occurs or risk is high.",
      "<b>Burn Dressings and Wound Care:</b> Non-adherent dressings, hydrogel dressings, biological dressings, wound irrigation solutions.",
      "<b>Tetanus Vaccine:</b> Booster may be needed if last vaccination >5–10 years ago or wound is contaminated."
    ],
"emergency": "\n  <b>If the burn covers a large area, looks charred, or exposes deeper tissue—seek emergency treatment immediately.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/burns.jpg"
  },

  "Cold": {
    "steps": [
      "<b>Rest and Hydration:</b> Drink water, herbal teas, clear broths; get plenty of rest.",
      "<b>Saline Nasal Irrigation:</b> Use saline spray or Neti pot to clear mucus.",
      "<b>Steam Inhalation:</b> Inhale steam from hot water or steamy shower; add eucalyptus or menthol if desired.",
      "<b>Humidify the Air:</b> Use humidifier or vaporizer.",
      "<b>Warm Compress:</b> Apply to face for sinus pressure relief.",
      "<b>Over-the-Counter Cold Medications:</b> Decongestants, antihistamines, cough suppressants, pain relievers.",
      "<b>Soothe a Sore Throat:</b> Gargle with warm salt water, use throat lozenges.",
      "<b>Elevate Your Head:</b> Helps nasal drainage while sleeping.",
      "<b>Practice Good Hygiene:</b> Wash hands, cover mouth when sneezing/coughing.",
      "<b>Stay Warm and Comfortable:</b> Dress warmly and avoid cold exposure."
    ],
    "medicine": [
      "<b>Pain Relievers and Fever Reducers:</b> Acetaminophen (Tylenol), Ibuprofen (Advil, Motrin).",
      "<b>Decongestants:</b> Pseudoephedrine (Sudafed), Phenylephrine; oral or nasal spray.",
      "<b>Antihistamines:</b> Diphenhydramine (Benadryl), Loratadine (Claritin), Cetirizine (Zyrtec).",
      "<b>Cough Suppressants:</b> Dextromethorphan (liquid syrups, lozenges, capsules).",
      "<b>Expectorants:</b> Guaifenesin (Mucinex).",
      "<b>Throat Lozenges or Sprays:</b> Menthol or benzocaine for soothing."
    ],
"emergency": "\n  <b>If the person has severe chills, confusion, or difficulty breathing—seek emergency care.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/cold.jpg"
  },

  "Choking": {
    "steps": [
      "<b>Assess the Situation:</b> Can the person speak, breathe, or cough? Encourage coughing if possible.",
      "<b>Perform the Heimlich Maneuver (Abdominal Thrusts):</b> Stand behind, make a fist, thrust inward and upward until object expelled.",
      "<b>Perform Back Blows and Chest Thrusts (Infants under 1 year):</b> 5 back blows, then 5 chest thrusts with two fingers.",
      "<b>Call for Emergency Assistance:</b> If airway blocked, call 911 immediately.",
      "<b>Perform CPR if necessary:</b> If person becomes unconscious and stops breathing, start CPR.",
      "<b>Follow Instructions from Emergency Services:</b> Continue first aid as instructed until help arrives."
    ],
    "medicine": [
      "<b>Bronchodilators:</b> For choking due to asthma or COPD. Short-acting (Albuterol) or long-acting (Formoterol, Salmeterol).",
      "<b>Epinephrine:</b> For anaphylaxis-induced choking, via auto-injector (EpiPen).",
      "<b>Sedatives or Muscle Relaxants:</b> For seizure or muscle spasm-induced airway obstruction, administered by healthcare professionals."
    ],
"emergency": "\n  <b>If the person cannot breathe, cough, or speak—this is a life-threatening emergency. Call for help immediately.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/choking.jpg"
  },

  "Cramps": {
    "steps": [
      "<b>Stop Activity:</b> Rest immediately.",
      "<b>Stretch and Massage:</b> Stretch gently, massage in circular motion for 20-30 seconds.",
      "<b>Apply Heat or Cold:</b> Warm compress to relax muscle, cold pack to reduce inflammation.",
      "<b>Hydrate:</b> Drink water or sports drinks with electrolytes.",
      "<b>Rehydrate and Replace Electrolytes:</b> Use electrolyte solutions or consume foods rich in potassium, calcium, magnesium, sodium.",
      "<b>Gentle Movement:</b> Stretch affected muscle after cramp subsides.",
      "<b>Prevention:</b> Stay hydrated, stretch regularly, warm up and cool down, maintain balanced diet, avoid overexertion, check medications."
    ],
    "medicine": [
      "<b>NSAIDs:</b> Ibuprofen (Advil, Motrin), Naproxen (Aleve).",
      "<b>Acetaminophen:</b> Tylenol.",
      "<b>Topical Analgesics:</b> Menthol-based creams like Icy Hot or Biofreeze, Capsaicin cream.",
      "<b>Muscle Relaxants:</b> Baclofen, Cyclobenzaprine (Flexeril).",
      "<b>Electrolyte Replacement Supplements:</b> Oral rehydration solutions or electrolyte tablets."
    ],
"emergency": "\n  <b>If cramps come with chest pain, dizziness, or sudden severe weakness—seek medical help.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/cramps.webp"
  },

  "Dry Cough": {
    "steps": [
      "<b>Stay Hydrated:</b> Drink water, herbal teas, or clear broths.",
      "<b>Use Humidifiers or Steam:</b> Moisten air to relieve throat irritation.",
      "<b>Gargle with Salt Water:</b> 1/4 to 1/2 tsp salt in warm water several times a day.",
      "<b>Lozenges or Hard Candy:</b> Soothe throat irritation and stimulate saliva.",
      "<b>Avoid Irritants:</b> Cigarette smoke, air pollutants, strong odors.",
      "<b>Use OTC Cough Suppressants:</b> Dextromethorphan or codeine as directed.",
      "<b>Consider Honey:</b> Mix with warm water or tea to soothe throat.",
      "<b>Rest and Relaxation:</b> Avoid activities that exacerbate coughing."
    ],
    "medicine": [
      "<b>Cough Suppressants (Antitussives):</b> Dextromethorphan in syrups or tablets.",
      "<b>Throat Lozenges or Sprays:</b> Menthol or benzocaine.",
      "<b>Expectorants:</b> Guaifenesin to thin mucus.",
      "<b>Decongestants:</b> Pseudoephedrine or Phenylephrine if nasal congestion is present.",
      "<b>Antihistamines:</b> Diphenhydramine or Cetirizine for allergy-related cough."
    ],
"emergency": "\n  <b>If cough includes blood, severe shortness of breath, chest pain, or high fever—seek emergency help.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/dry_cough.jpg"
  },
  
  "Fracture": {
    "steps": [
      "<b>Assess the Situation:</b> Stay calm and assess the severity of the injury. Avoid moving the injured area unnecessarily.",
      "<b>Immobilize the Injured Area:</b> Stabilize the limb using splints or supports without manipulating the fracture.",
      "<b>Apply Cold Compress:</b> Use a cold pack for 15-20 minutes at a time to reduce swelling.",
      "<b>Elevate the Injured Limb:</b> Raise above heart level if possible to reduce swelling.",
      "<b>Control Bleeding (if present):</b> Apply gentle pressure with a clean cloth or gauze.",
      "<b>Provide Comfort and Support:</b> Stay with the injured person, keep them calm and warm.",
      "<b>Do Not Give Food or Drink (if surgery is likely):</b> Avoid food or drink in case anesthesia is needed."
    ],
    "medicine": [
      "<b>Pain Relievers:</b> Acetaminophen or ibuprofen to alleviate pain and inflammation.",
      "<b>Prescription Pain Medications:</b> Opioids like oxycodone or hydrocodone if severe pain persists.",
      "<b>Nonsteroidal Anti-Inflammatory Drugs (NSAIDs):</b> Reduce inflammation and pain.",
      "<b>Muscle Relaxants:</b> Support healing by reducing muscle tension.",
      "<b>Bone Health Supplements:</b> Calcium and vitamin D to promote bone repair.",
      "<b>Bisphosphonates:</b> Prevent bone loss in osteoporosis patients.",
      "<b>Calcitonin:</b> Reduce bone pain and improve bone density.",
      "<b>Antibiotics:</b> Prevent infection in open fractures."
    ],
"emergency": "\n  <b>If the bone is visibly deformed, breaking through the skin, or the person is in severe pain—seek urgent medical attention.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/fracture.jpg"
  },

  "Head Injuries": {
    "steps": [
      "<b>Assess the Situation:</b> Check consciousness, responsiveness, and visible injuries.",
      "<b>Ensure Safety:</b> Move the person to a safe area if possible without causing harm.",
      "<b>Call for Medical Assistance:</b> Contact emergency services immediately if severe.",
      "<b>Stabilize the Person:</b> Keep them still and comfortable.",
      "<b>Control Bleeding (if present):</b> Apply gentle pressure without pressing on the skull.",
      "<b>Monitor for Signs of Serious Injury:</b> Watch for loss of consciousness, confusion, vomiting, abnormal pupils, seizures, or weakness.",
      "<b>Provide Comfort and Reassurance:</b> Keep the person calm.",
      "<b>Do Not Remove Protective Headgear:</b> Keep helmet on unless absolutely necessary."
    ],
    "medicine": [
      "<b>Initial Assessment and Stabilization:</b> Check vital signs and neurological status.",
      "<b>Emergency Medical Care:</b> Transport to hospital if moderate to severe injury.",
      "<b>Imaging Studies:</b> CT or MRI to identify internal damage.",
      "<b>Pain Management:</b> OTC pain relievers like acetaminophen or ibuprofen; opioids if severe.",
      "<b>Anti-Seizure Medications:</b> Prevent seizures after severe head injury.",
      "<b>Corticosteroids:</b> Reduce brain swelling if indicated.",
      "<b>Antibiotics:</b> Only if infection risk exists.",
      "<b>Monitoring and Observation:</b> Track neurological changes.",
      "<b>Rehabilitation:</b> Recovery of cognitive or physical deficits as needed."
    ],
"emergency": "\n  <b>If the person loses consciousness, vomits, or becomes confused—seek emergency help immediately.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/head_injuries.jpg"
  },

  "Heat Exhaustion": {
    "steps": [
      "<b>Move to a Cooler Environment:</b> Shade, air-conditioning, and removal of excess clothing.",
      "<b>Hydrate:</b> Drink cool water or electrolyte drinks.",
      "<b>Rest and Cool Down:</b> Use wet cloths, cool shower, fan, or ice packs on neck/armpits/groin.",
      "<b>Monitor Symptoms:</b> Watch for heatstroke signs like confusion, rapid heartbeat, vomiting, dizziness.",
      "<b>Rehydrate and Replace Electrolytes:</b> Drink electrolyte solutions.",
      "<b>Prevent Future Incidents:</b> Hydrate, take breaks, wear light clothing, avoid peak heat."
    ],
    "medicine": [
      "<b>Oral Rehydration Solutions:</b> Pedialyte, Gatorade to replace fluids and electrolytes.",
      "<b>Intravenous (IV) Fluids:</b> Hospital-administered saline for severe dehydration.",
      "<b>Medications for Symptomatic Relief:</b> NSAIDs for headache/muscle aches, acetaminophen for mild fever.",
      "<b>Antiemetics (if Nausea or Vomiting):</b> Ondansetron or Metoclopramide.",
      "<b>Pain Medications (for Muscle Cramps):</b> Muscle relaxants such as Cyclobenzaprine or Baclofen."
    ],
"emergency": "\n  <b>If there is fainting, confusion, or hot dry skin—this may be heatstroke. Seek emergency care at once.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/heat_exhaustion.jpg"
  },

  "Laceration": {
    "steps": [
      "<b>Assess the Severity of the Laceration:</b> Check depth, bleeding, foreign objects, infection signs.",
      "<b>Control Bleeding:</b> Apply direct pressure and elevate the area.",
      "<b>Clean the Wound:</b> Rinse gently with clean water.",
      "<b>Assess for Foreign Objects:</b> Do not remove embedded objects yourself.",
      "<b>Close the Wound (if necessary):</b> Use adhesive strips, sutures, or staples if required.",
      "<b>Apply a Bandage or Dressing:</b> Protect the wound and absorb drainage.",
      "<b>Pain Management:</b> Use OTC pain relievers as needed."
    ],
    "medicine": [
      "<b>Topical Antibiotics:</b> Bacitracin or Neosporin to prevent infection.",
      "<b>Topical Anesthetics:</b> Lidocaine or benzocaine for numbing.",
      "<b>Pain Relievers:</b> Acetaminophen or ibuprofen.",
      "<b>Tetanus Vaccination:</b> If wound is contaminated or last shot >5 years.",
      "<b>Prescription Medications:</b> Oral antibiotics if deep/contaminated.",
      "<b>Anticoagulants or Antiplatelet Medications:</b> Adjust if necessary due to bleeding risk."
    ],
"emergency": "\n  <b>If the cut is deep, bleeding heavily, or exposing muscle or bone—seek immediate treatment.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/laceration.jpg"
  },

  "Menstrual Cramps": {
    "steps": [
      "<b>Apply Heat Therapy:</b> Use heating pad or warm compress on lower abdomen.",
      "<b>Practice Relaxation Techniques:</b> Deep breathing, yoga, or meditation.",
      "<b>Take Over-the-Counter Pain Relievers:</b> NSAIDs such as ibuprofen or naproxen.",
      "<b>Stay Hydrated:</b> Drink plenty of water.",
      "<b>Eat a Balanced Diet:</b> Consume nutritious foods, avoid excess caffeine or sugar.",
      "<b>Try Herbal Remedies:</b> Chamomile, ginger, or peppermint tea.",
      "<b>Practice Gentle Exercise:</b> Walking, swimming, or stretching.",
      "<b>Take Warm Baths:</b> Helps relax muscles.",
      "<b>Use Essential Oils:</b> Lavender or clary sage for aromatherapy.",
      "<b>Consider Hormonal Birth Control:</b> Consult healthcare provider for hormonal options."
    ],
    "medicine": [
      "<b>Nonsteroidal Anti-Inflammatory Drugs (NSAIDs):</b> Ibuprofen, naproxen, aspirin to reduce inflammation and pain.",
      "<b>Acetaminophen:</b> Tylenol for pain relief.",
      "<b>Menstrual Pain Relief Formulations:</b> Midol, Pamprin, Advil Menstrual Pain."
    ],
"emergency": "\n  <b>If cramps are unusually severe, accompanied by heavy bleeding or dizziness—seek medical care.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/menstrual_cramps.jpg"
  },

  "Minor Cuts and Scrapes": {
    "steps": [
      "<b>Assess the Injury:</b> Determine severity and whether home care is sufficient.",
      "<b>Stop the Bleeding:</b> Apply gentle pressure, elevate if possible.",
      "<b>Clean the Wound:</b> Use clean water, mild soap around the wound.",
      "<b>Cover the Wound:</b> Use adhesive bandage or sterile gauze.",
      "<b>Change the Dressing:</b> At least once a day or when wet/soiled.",
      "<b>Monitor for Signs of Infection:</b> Watch for redness, swelling, warmth, pus.",
      "<b>Pain Management:</b> OTC pain relievers like acetaminophen or ibuprofen.",
      "<b>Rest and Protect the Wound:</b> Avoid friction or pressure on the wound."
    ],
    "medicine": [
      "<b>Antibiotic Ointments:</b> Bacitracin or Neosporin.",
      "<b>Antiseptic Solutions:</b> Hydrogen peroxide or Betadine.",
      "<b>Pain Relievers:</b> Acetaminophen or ibuprofen.",
      "<b>Topical Anesthetics:</b> Benzocaine or lidocaine.",
      "<b>Sterile Gauze Pads and Adhesive Bandages:</b> Protect and cover the wound."
    ],
"emergency": "\n  <b>If bleeding does not stop or the wound shows signs of infection—seek medical help.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/minor_cuts_scrapes.webp"
  },

  "Nosebleeds": {
    "steps": [
      "<b>Stay Calm:</b> Most nosebleeds are manageable.",
      "<b>Sit Up Straight:</b> Lean slightly forward.",
      "<b>Pinch the Nose:</b> Apply firm pressure for 10-15 minutes.",
      "<b>Breathe Through Your Mouth:</b> Avoid inhaling blood.",
      "<b>Do Not Lie Down:</b> Avoid increasing blood flow to the nose.",
      "<b>Apply Cold Compress:</b> Constricts blood vessels and reduces bleeding.",
      "<b>Avoid Blowing Your Nose:</b> Prevents dislodging clots.",
      "<b>Monitor the Bleeding:</b> Track duration and blood loss.",
      "<b>Avoid Certain Activities:</b> Avoid strenuous activities during and after."
    ],
    "medicine": [
      "<b>Topical Nasal Decongestants:</b> Oxymetazoline or phenylephrine.",
      "<b>Topical Nasal Steroids:</b> Fluticasone or mometasone for inflammation.",
      "<b>Moisturizing Nasal Saline Sprays:</b> Keep nasal passages hydrated.",
      "<b>Antifibrinolytic Agents:</b> Tranexamic acid if recurrent/severe.",
      "<b>Systemic Medications:</b> Treat underlying conditions like hypertension or bleeding disorders."
    ],
"emergency": "\n  <b>If the nosebleed lasts more than 20 minutes or happened after a head injury—seek emergency assistance.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/nosebleeds.jpg"
  },

  "Open Wounds": {
    "steps": [
      "<b>Protect Yourself:</b> Before providing first aid to the person with the open wound, make sure to wear disposable gloves or wash your hands thoroughly with soap and water to prevent the spread of infection.",
      "<b>Control Bleeding:</b> Apply direct pressure to the wound using a clean cloth or sterile gauze pad to control bleeding. Maintain pressure for several minutes until bleeding stops. Elevate the injured area if possible to help reduce blood flow.",
      "<b>Clean the Wound:</b> Rinse the wound gently with clean water to remove any dirt, debris, or foreign objects. Avoid using soap directly on the wound, as it may irritate the tissue. If available, use a sterile saline solution for cleaning.",
      "<b>Remove Debris:</b> Use tweezers cleaned with alcohol to carefully remove any visible debris or foreign objects from the wound. Be gentle to avoid causing further injury or pushing debris deeper into the tissue.",
      "<b>Cover the Wound:</b> Once the wound is clean and dry, cover it with a sterile adhesive bandage or gauze pad to protect it from further contamination and promote healing. Change the bandage daily or as needed.",
      "<b>Monitor for Signs of Infection:</b> Keep an eye on the wound for any signs of infection, such as increased redness, swelling, warmth, pain, or pus. If you notice any signs of infection, seek medical attention."
    ],
    "medicine": [
      "<b>Antibiotic Ointments:</b> Over-the-counter antibiotic ointments, such as Neosporin, Polysporin, or Bacitracin, can be applied to the cleaned wound to help prevent infection and promote healing.",
      "<b>Antiseptic Solutions:</b> Antiseptic solutions, such as hydrogen peroxide or povidone-iodine (Betadine), can be used to clean the wound and reduce the risk of infection.",
      "<b>Saline Solution:</b> Sterile saline solution or wound wash can be used to irrigate and clean the wound. It helps remove debris and bacteria from the wound without damaging the tissue.",
      "<b>Pain Relievers:</b> Over-the-counter pain relievers, such as acetaminophen (Tylenol) or ibuprofen (Advil, Motrin), may be taken as directed to alleviate any pain or discomfort associated with the wound.",
      "<b>Topical Analgesics:</b> Topical analgesic creams or gels containing ingredients like lidocaine or benzocaine can be applied to the skin surrounding the wound to provide localized pain relief.",
      "<b>Hydrogel Dressings:</b> Hydrogel dressings are moist wound dressings that help keep the wound bed hydrated and promote healing.",
      "<b>Silver-based Dressings:</b> Silver-based dressings have antimicrobial properties and can help prevent infection in open wounds.",
      "<b>Honey-based Products:</b> Medical-grade honey-based products, such as honey ointments or dressings, have natural antimicrobial properties and can help promote wound healing."
    ],
"emergency": "\n  <b>If the wound is deep, contaminated, or difficult to close—seek medical attention immediately.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/open_wounds.jpeg"
  },

  "Shoulder Dislocation": {
    "steps": [
      "<b>Stop Activity:</b> If you suspect a dislocation, stop any activity immediately to prevent further injury or damage to the affected joint.",
      "<b>Immobilize the Joint:</b> Immobilize the affected joint to prevent movement and further aggravation of the dislocation. You can use a splint, sling, or any rigid object to stabilize the joint.",
      "<b>Apply Ice:</b> Apply ice or a cold pack wrapped in a cloth to the affected area to help reduce swelling and alleviate pain. Apply the ice for 15-20 minutes at a time, several times a day.",
      "<b>Do Not Attempt Self-Reduction:</b> Attempting to relocate (reduce) a dislocated joint without proper training or medical supervision can cause further injury or complications.",
      "<b>Avoid Stress on the Joint:</b> After the dislocation has been reduced and stabilized, avoid putting stress on the affected joint to allow it to heal properly.",
      "<b>Prevent Recurrence:</b> Follow preventive measures recommended by your healthcare provider to reduce the risk of future dislocations."
    ],
    "medicine": [
      "<b>Pain Relievers:</b> NSAIDs (ibuprofen, naproxen) or acetaminophen (Tylenol) for pain and inflammation.",
      "<b>Muscle Relaxants:</b> May be prescribed to alleviate muscle spasms and stiffness.",
      "<b>Prescription Pain Medications:</b> Stronger pain medications, such as opioids, may be used for severe pain.",
      "<b>Anti-Anxiety Medications:</b> To alleviate emotional distress associated with the injury.",
      "<b>Corticosteroids:</b> In certain situations, may be administered to reduce swelling and inflammation."
    ],
"emergency": "\n  <b>If there is numbness, severe pain, or visible deformity—seek emergency care.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/shoulder_dislocation.jpg"
  },

  "Sore Throat": {
    "steps": [
      "<b>Stay Hydrated:</b> Drink plenty of fluids, such as water, herbal teas, warm broths, and non-caffeinated beverages.",
      "<b>Gargle with Warm Salt Water:</b> Mix about half a teaspoon of salt into a glass of warm water, gargle for 30 seconds, then spit it out.",
      "<b>Use Throat Lozenges or Hard Candy:</b> Sucking on lozenges or candy can help keep your throat moist and relieve discomfort.",
      "<b>Stay Away from Irritants:</b> Avoid smoking, secondhand smoke, and other irritants.",
      "<b>Use a Humidifier:</b> Adds moisture to the air to soothe a dry, irritated throat.",
      "<b>Rest Your Voice:</b> Reduce strain on your throat by speaking softly.",
      "<b>Avoid Allergens:</b> Try to avoid exposure to allergens if your sore throat is allergy-related."
    ],
    "medicine": [
      "<b>Pain Relievers:</b> Acetaminophen, ibuprofen, or naproxen to reduce pain and inflammation.",
      "<b>Throat Lozenges or Sprays:</b> Containing menthol, benzocaine, or eucalyptus to numb and soothe the throat.",
      "<b>Warm Salt Water Gargle:</b> Reduces inflammation and kills bacteria.",
      "<b>Honey:</b> Has natural antibacterial and soothing properties.",
      "<b>Over-the-Counter Lozenges and Sprays:</b> For temporary relief from throat pain.",
      "<b>Decongestants:</b> If postnasal drip is present, such as pseudoephedrine or phenylephrine.",
      "<b>Antihistamines:</b> If sore throat is allergy-related, such as loratadine or cetirizine."
    ],
"emergency": "\n  <b>If there is difficulty breathing, drooling, or inability to swallow—seek urgent medical help.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/sore_throat.jpg"
  },

  "Splinter": {
    "steps": [
      "<b>Assess the Splinter:</b> Determine the size, depth, and location of the splinter. Check for signs of infection such as redness, swelling, warmth, or pus.",
      "<b>Clean the Area:</b> Wash hands thoroughly with soap and water before handling the splinter. Clean the area around the splinter to remove dirt or bacteria.",
      "<b>Inspect the Splinter:</b> Use a magnifying glass if necessary to see the direction the splinter entered the skin.",
      "<b>Remove the Splinter:</b> Use clean tweezers to gently pull out the splinter in the same direction it entered. Avoid squeezing or breaking it. Seek medical help if deeply embedded.",
      "<b>Clean the Wound:</b> After removal, wash the area with soap and water or use an antiseptic solution.",
      "<b>Cover the Wound:</b> If bleeding, apply a clean bandage to protect it.",
      "<b>Monitor for Signs of Infection:</b> Watch for redness, swelling, warmth, pain, or pus and seek medical attention if noticed."
    ],
    "medicine": [
      "<b>Topical Antibiotic Ointment:</b> Apply bacitracin or Neosporin to prevent infection.",
      "<b>Antiseptic Solution:</b> Clean with hydrogen peroxide or povidone-iodine to disinfect.",
      "<b>Pain Relievers:</b> Acetaminophen or ibuprofen may be taken as needed.",
      "<b>Anti-inflammatory Cream:</b> Hydrocortisone cream may reduce inflammation and soothe the skin.",
      "<b>Tetanus Vaccination:</b> Get a tetanus shot if it’s been over five years or if the splinter came from a dirty source."
    ],
"emergency": "\n  <b>If the splinter is deeply embedded, infected, or near the eye—seek medical care.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/splinter.jpg"
  },

  "Sprain": {
    "steps": [
      "<b>Rest:</b> Stop the activity and avoid putting weight on the injured area.",
      "<b>Ice:</b> Apply a cold pack for 15-20 minutes several times a day to reduce swelling.",
      "<b>Compression:</b> Wrap the injured area with an elastic bandage to reduce swelling and provide support.",
      "<b>Elevation:</b> Raise the limb above heart level to reduce swelling.",
      "<b>Immobilization:</b> Use a splint or brace if necessary, following professional guidance.",
      "<b>Physical Therapy:</b> Begin gentle range-of-motion exercises once pain and swelling subside.",
      "<b>Restoration of Function:</b> Gradually return to normal activities and exercise as tolerated.",
      "<b>Prevention:</b> Wear appropriate footwear, use protective equipment, and practice proper techniques."
    ],
    "medicine": [
      "<b>NSAIDs:</b> Ibuprofen or naproxen to reduce pain, swelling, and inflammation.",
      "<b>Acetaminophen:</b> For pain relief without anti-inflammatory effect.",
      "<b>Topical Pain Relievers:</b> Creams or gels with menthol, lidocaine, or capsaicin.",
      "<b>Prescription Medications:</b> Stronger pain medications or corticosteroids for severe cases.",
      "<b>Muscle Relaxants:</b> To relieve spasms contributing to pain.",
      "<b>Antibiotics:</b> Only if sprain is accompanied by open wounds at risk of infection."
    ],
"emergency": "\n  <b>If there is severe swelling, inability to bear weight, or possible fracture—seek medical evaluation.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/sprain.jpg"
  },

  "Superficial Injuries": {
    "steps": [
      "<b>Clean the Wound:</b> Wash hands, gently clean the wound with mild soap and water, and pat dry.",
      "<b>Cover the Wound:</b> Use a sterile bandage, gauze, or adhesive strip to protect it. Change regularly.",
      "<b>Monitor for Signs of Infection:</b> Watch for redness, swelling, warmth, pain, or pus.",
      "<b>Rest and Protect the Wound:</b> Avoid activities that may worsen the injury. Protect it from friction or pressure.",
      "<b>Keep the Wound Moist:</b> Apply antibiotic ointment to promote healing and prevent infection."
    ],
    "medicine": [
      "<b>Apply Antiseptic:</b> Hydrogen peroxide, povidone-iodine, or antiseptic sprays/ointments.",
      "<b>Pain Relief:</b> Acetaminophen or ibuprofen for pain or discomfort.",
      "<b>Antibiotic Ointments:</b> Neosporin or Polysporin to prevent infection.",
      "<b>Topical Analgesics:</b> Creams or gels containing lidocaine or benzocaine for localized pain relief."
    ],
"emergency": "\n  <b>If pain worsens or signs of infection appear—seek medical help.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/superficial_injuries.jpg"
  },

  "Tonsillitis": {
    "steps": [
      "<b>Rest and Hydration:</b> Get plenty of rest and drink fluids to stay hydrated and soothe the throat.",
      "<b>Salt Water Gargle:</b> Gargle with warm salt water several times a day.",
      "<b>Humidify the Air:</b> Use a humidifier to keep air moist and soothe irritation.",
      "<b>Avoid Irritants:</b> Avoid smoking and other irritants.",
      "<b>Rest Your Voice:</b> Speak softly and avoid shouting.",
      "<b>Warm Compress:</b> Apply a warm compress to the neck to reduce pain and swelling."
    ],
    "medicine": [
      "<b>Antibiotics:</b> Prescribed for bacterial tonsillitis (penicillin, amoxicillin, or azithromycin). Complete the full course.",
      "<b>Pain Relievers and Fever Reducers:</b> Acetaminophen or ibuprofen to reduce pain, fever, and inflammation.",
      "<b>Throat Lozenges or Sprays:</b> Containing benzocaine, menthol, or phenol for temporary relief.",
      "<b>Corticosteroids:</b> For severe inflammation, short-term oral or injected treatment.",
      "<b>Antiviral Medications:</b> For viral tonsillitis in specific cases.",
      "<b>Antiseptic Mouthwash or Gargle:</b> Chlorhexidine or povidone-iodine to reduce bacteria and promote healing.",
      "<b>Antihistamines:</b> Diphenhydramine or loratadine if allergies contribute.",
      "<b>Fluids and Hydration:</b> Drink plenty of fluids to stay hydrated and soothe the throat."
    ],
"emergency": "\n  <b>If there is trouble breathing, drooling, or extremely swollen tonsils—seek emergency care.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",    "visual": "images/tonsillitis.jpeg"
  },

  "Wet Cough": {
    "steps": [
      "<b>Stay Hydrated:</b> Drink plenty of fluids to loosen mucus and keep airways hydrated.",
      "<b>Use a Humidifier:</b> Adds moisture to the air to loosen mucus and soothe airways.",
      "<b>Steam Inhalation:</b> Inhale steam to help relieve chest congestion.",
      "<b>Gargle with Salt Water:</b> Soothes throat irritation caused by coughing.",
      "<b>Practice Postural Drainage:</b> Change positions to help drain mucus from lungs.",
      "<b>Coughing Technique:</b> Use deep breaths and forceful coughing to clear mucus.",
      "<b>Expectorants:</b> Medications like guaifenesin to thin mucus.",
      "<b>Avoid Irritants:</b> Stay away from smoke, pollutants, and other irritants.",
      "<b>Rest and Stay Warm:</b> Rest to help the body fight the underlying cause."
    ],
    "medicine": [
      "<b>Expectorants:</b> Guaifenesin to loosen and expel mucus.",
      "<b>Mucolytics:</b> Acetylcysteine to thin and loosen thick mucus.",
      "<b>Cough Suppressants:</b> Dextromethorphan for occasional nighttime use.",
      "<b>Bronchodilators:</b> Albuterol if associated with asthma or COPD.",
      "<b>Antibiotics:</b> If a bacterial infection is present, like bronchitis or pneumonia.",
      "<b>Steroids:</b> For severe inflammation in the airways.",
      "<b>Antihistamines:</b> Loratadine or cetirizine if allergies contribute to symptoms."
    ],
   "emergency": "\n  <b>If cough includes blood, shortness of breath, chest pain, or high fever—seek emergency help immediately.</b>\n  \n  <div class=\"hotline-list\">\n    <p><strong>Philippine Emergency Hotlines:</strong></p>\n    <ul>\n      <li><b>National Emergency Hotline:</b> 911</li>\n      <li><b>Police:</b> 117</li>\n      <li><b>Bureau of Fire Protection (BFP):</b> (02) 8426-0219</li>\n      <li><b>Philippine Red Cross:</b> 143</li>\n      <li><b>DOH Health Emergency:</b> (02) 8651-7800</li>\n    </ul>\n  </div>\n\n  <p><b>Emergency Note:</b> Call 911 or the appropriate hotline if the situation is life-threatening.</p>",
    "visual": "images/wet_cough.jpeg"
  }
}

@app.route('/get_data')
def get_data():
    return jsonify(firstAidData)

@app.route('/firstaid.html')
def firstaid():
    return send_from_directory('.', 'firstaid.html')

@app.route('/detail.html')
def detail():
    return send_from_directory('.', 'detail.html')

@app.route('/index.html')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


