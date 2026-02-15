def qurey_prompt(prompt_name: str, clause = ''):

    prompt = ''

    if prompt_name == 'structured_cot_prompt':
        prompt= f'''Classify the following sentence from a Terms of Service document into one of the predefined categories.
        Options:
        ["Arbitration", "Unilateral change", "Content removal", "Jurisdiction", "Choice of law", "Limitation of liability", "Unilateral termination", "Contract by using", "Other"]

        The sentence may describe a potentially unfair clause or a fair/neutral clause.
        The eight specific categories correspond to types of potentially unfair clauses.
        If the sentence does not correspond to any of these eight types, it should be classified as "Other", which represents fair or neutral clauses.

        Response Instructions:
        Provide your response strictly in valid JSON format with ALL 4 fields shown below.
        1. "legal_principle": a brief statement of the relevant legal principle
        2. "power_imbalance": a concise assessment of whether the clause creates a power imbalance
        3. "consumer_business_harm ": a concise description of potential consumer/business harm
        4. "final_decision": You MUST respond with EXACTLY one of these options (copy-paste exactly)

        Examples:
        Clause:
        "arbitration notice : unless you opt out of arbitration within 30 days of the date you first agree to these terms by following the opt-out procedure specified in the `` arbitration \'\' section below , and except for certain types of disputes described in the `` arbitration `` section below , you agree that disputes between you and academia.edu will be resolved by binding , individual arbitration and you are waiving your right to a trial by jury or to participate as a plaintiff or class member in any purported class action or representative proceeding .”

        {{
          "legal_principle": "Mandatory arbitration clauses can lawfully replace or delay court litigation if consent is properly obtained.",
          "power_imbalance": "The clause limits the consumer’s procedural rights by defaulting or exclusively requiring submission of disputes to arbitration unless actively opted out.",
          "consumer_business_harm": "Consumers may lose access to courts, jury trials, and collective actions, reducing their ability to effectively pursue claims.",
          "final_decision": "Arbitration"
        }}

        Clause:
        "academia.edu reserves the right , at its sole discretion , to modify the site , services and these terms , at any time and without prior notice ."
        Response:
        {{
          "legal_principle": "Contract law generally requires reasonable notice and mutual consent for material contractual modifications.",
          "power_imbalance": "The business retains sole discretion to change terms without notice, leaving consumers unable to negotiate or respond, or at risk of losing the contracted service.",
          "consumer_business_harm": "Consumers may be bound by unfavorable changes they were not aware of or did not agree to.",
          "final_decision": "Unilateral change"
        }}
        
        Clause:
        "amazon reserves the right ( but not the obligation ) to remove or edit such content , but does not regularly review posted content ."
        Response:
        {{
          "legal_principle": "Service providers may reserve moderation, modification or deletion rights over user-generated content.",
          "power_imbalance": "The provider has unilateral control over content removal without a corresponding obligation to review or justify decisions or provide notice.",
          "consumer_business_harm": "Users risk arbitrary removal of content or loss of visibility without recourse or explanation.",
          "final_decision": "Content removal"
        }}
        
        Clause:         
        "academia.edu with an arbitration opt-out notice , any dispute other than an individual action brought in small claims court , will be the state and federal courts located in the northern district of california and each of the parties hereto waives any objection to jurisdiction and venue in such courts ."
        Response: 
        {{
          "legal_principle": "Parties may contractually agree to a specific forum for resolving disputes.",
          "power_imbalance": "The clause imposes a fixed jurisdiction that may be inconvenient or inaccessible for consumers, or otherwise unreasonable, unfair or unjust.",
          "consumer_business_harm": "Consumers may face increased costs and practical barriers when bringing claims in a distant forum.",
          "final_decision": "Jurisdiction"
        }}
        
        Clause:         
        "these terms and any action related thereto will be governed by the laws of the state of california without regard to its conflict of laws provisions ."
        Response:         
        {{
          "legal_principle": "Contracts may designate the governing law applicable to disputes.",
          "power_imbalance": "The business selects a governing law that may favor its interests over consumer protections.",
          "consumer_business_harm": "Consumers may lose the benefit of more protective local laws applicable in their jurisdiction.",
          "final_decision": "Choice of law"
        }}
        
        Clause:         
        "neither academia.edu nor any other person or entity involved in creating , producing , or delivering the site , services or collective content will be liable for any incidental , special , exemplary or consequential damages , or lost profits , loss of data or loss of goodwill , service interruption , computer damage or system failure or the cost of substitute products or services , or for any damages for personal or bodily injury or emotional distress arising out of or in connection with these terms or from the use of or inability to use the site , services or collective content , or from any communications , interactions or meetings with other users of the site or services or other persons with whom you communicate or interact as a result of your use of the site or services , whether based on warranty , contract , tort ( including negligence ) , product liability or any other legal theory , whether or not academia.edu has been informed of the possibility of such damage , and whether or not foreseeable , even if a limited remedy set forth herein is found to have failed of its essential purpose ."          
        Response:         
        {{
          "legal_principle": "Limitation of liability clauses restrict the scope of damages a party may claim.",
          "power_imbalance": "The clause broadly shields the business from liability while leaving consumers exposed to losses.",
          "consumer_business_harm": "Consumers may be unable to recover compensation even for foreseeable or serious harm.",
          "final_decision": "Limitation of liability"
        }}
        
        Clause:         
        "academia.edu reserves the right to suspend or terminate your account if any information provided during the registration process or thereafter proves to be inaccurate , not current or incomplete ."          
        Response:         
        {{
          "legal_principle": "Service providers may terminate contracts under specified conditions.",
          "power_imbalance": "The business has unilateral authority to suspend or terminate accounts based on its own assessment.",
          "consumer_business_harm": "Consumers may lose access to services or data without meaningful opportunity to contest termination.",
          "final_decision": "Unilateral termination"
        }}
        
        Clause:         
        "you acknowledge and agree that , by accessing or using the site or services or by downloading or posting any content from or on the site or through the services , you are indicating that you have read , and that you understand and agree to be bound by , these terms , whether or not you have registered on or through the site ."          
        Response:         
        {{
          "legal_principle": "A user may become bound to the terms through mere use of the service.",
          "power_imbalance": "Creates a take-it-or-leave-it dynamic that may be repeated whenever the the provider updates terms without notice or negotiation.",
          "consumer_business_harm": "Consumers may unknowingly lose rights or accept obligations access to services or data without meaningful opportunity to negotiate or contest termination.",
          "final_decision": "Contract by using"
        }}
        
        Clause:         
        "last updated date : may 15 , 2017"          
        Response:         
        {{
          "legal_principle": "Informational statements do not create contractual rights or obligations.",
          "power_imbalance": "The clause does not alter the balance of rights between the parties.",
          "consumer_business_harm": "No direct consumer or business harm arises from a purely informational update notice.",
          "final_decision": "Other"
        }}

        Now, classify the following clause.
        Clause:
        "{clause}"
        '''
    
    elif prompt_name == 'concise_cot_prompt':
        prompt= f'''Classify the following sentence from a Terms of Service document into one of the predefined categories.
        Options:
        ["Arbitration", "Unilateral change", "Content removal", "Jurisdiction", "Choice of law", "Limitation of liability", "Unilateral termination", "Contract by using", "Other"]

        The sentence may describe a potentially unfair clause or a fair/neutral clause.
        The eight specific categories correspond to types of potentially unfair clauses.
        If the sentence does not correspond to any of these eight types, it should be classified as "Other", which represents fair or neutral clauses.

        Response Instructions:
        Provide your response strictly in valid JSON format with ALL 2 fields shown below:
        - "justification": a brief, high-level legal justification (1–2 sentences)
        - "final_decision": You MUST respond with EXACTLY one of these options (copy-paste exactly)

        Examples:

        Clause:
        "arbitration notice : unless you opt out of arbitration within 30 days of the date you first agree to these terms by following the opt-out procedure specified in the `` arbitration '' section below , and except for certain types of disputes described in the `` arbitration `` section below , you agree that disputes between you and academia.edu will be resolved by binding , individual arbitration and you are waiving your right to a trial by jury or to participate as a plaintiff or class member in any purported class action or representative proceeding ."

        Response:
        {{
        "justification": "This clause requires disputes to be resolved through binding arbitration and explicitly waives the consumer’s right to a jury trial or class action, which limits access to judicial remedies and collective redress.",
        "final_decision": "Arbitration"
        }}

        Clause:
        "academia.edu reserves the right , at its sole discretion , to modify the site , services and these terms , at any time and without prior notice ."

        Response:
        {{
        "justification": "This clause allows the service provider to modify the terms or services at its sole discretion without prior notice, creating a power imbalance by preventing users from meaningfully consenting to future changes.",
        "final_decision": "Unilateral change"
        }}

        Clause:
        "amazon reserves the right ( but not the obligation ) to remove or edit such content , but does not regularly review posted content ."

        Response:
        {{
        "justification": "This clause grants the platform broad discretion to remove or edit user content without obligation or consistent oversight, enabling arbitrary enforcement that may undermine users’ expressive or reliance interests.",
        "final_decision": "Content removal"
        }}

        Clause:
        "academia.edu with an arbitration opt-out notice , any dispute other than an individual action brought in small claims court , will be the state and federal courts located in the northern district of california and each of the parties hereto waives any objection to jurisdiction and venue in such courts ."

        Response:
        {{
        "justification": "This clause mandates that disputes be litigated exclusively in a specific geographic forum, potentially burdening users by forcing them to pursue claims in an inconvenient or distant court.",
        "final_decision": "Jurisdiction"
        }}
        
        Clause:
        "these terms and any action related thereto will be governed by the laws of the state of california without regard to its conflict of laws provisions ."

        Response:
        {{
        "justification": "This clause unilaterally selects the governing law for all disputes, which may deprive users of protections available under their local or more consumer-favorable legal regimes.",
        "final_decision": "Choice of law"
        }}
        
        Clause:
        "neither academia.edu nor any other person or entity involved in creating , producing , or delivering the site , services or collective content will be liable for any incidental , special , exemplary or consequential damages , or lost profits , loss of data or loss of goodwill , service interruption , computer damage or system failure or the cost of substitute products or services , or for any damages for personal or bodily injury or emotional distress arising out of or in connection with these terms or from the use of or inability to use the site , services or collective content , or from any communications , interactions or meetings with other users of the site or services or other persons with whom you communicate or interact as a result of your use of the site or services , whether based on warranty , contract , tort ( including negligence ) , product liability or any other legal theory , whether or not academia.edu has been informed of the possibility of such damage , and whether or not foreseeable , even if a limited remedy set forth herein is found to have failed of its essential purpose ."

        Response:
        {{
        "justification": "This clause broadly excludes liability for a wide range of damages, including foreseeable harm, significantly restricting the provider’s legal accountability even in cases of negligence.",
        "final_decision": "Limitation of liability"
        }}
        
        Clause:
        "academia.edu reserves the right to suspend or terminate your account if any information provided during the registration process or thereafter proves to be inaccurate , not current or incomplete ."

        Response:
        {{
        "justification": This clause allows the provider to suspend or terminate user accounts based on subjective or loosely defined criteria, giving the provider disproportionate control without procedural safeguards.",
        "final_decision": "Unilateral termination"
        }}
        
        Clause:
        "you acknowledge and agree that , by accessing or using the site or services or by downloading or posting any content from or on the site or through the services , you are indicating that you have read , and that you understand and agree to be bound by , these terms , whether or not you have registered on or through the site ."

        Response:
        {{
        "justification": "This clause treats mere use of the service as binding acceptance of the terms, effectively imposing contractual obligations without explicit or informed consent.",
        "final_decision": "Contract by using"
        }}
        
        Clause:
        "last updated date : may 15 , 2017"

        Response:
        {{
        "justification": "This clause merely provides informational metadata (e.g., last updated date) and does not impose rights, obligations, or restrictions on either party.",
        "final_decision": "Other"
        }}
        
        Now, classify the following clause.
        Clause:
        "{clause}"
        '''
        
    return prompt
