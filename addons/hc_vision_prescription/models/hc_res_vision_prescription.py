# -*- coding: utf-8 -*-

from openerp import models, fields, api

class VisionPrescription(models.Model):    
    _name = "hc.res.vision.prescription"    
    _description = "Vision Prescription"        

    identifier_ids = fields.One2many(comodel_name="hc.vision.prescription.identifier", inverse_name="vision_prescription_id", string="Identifiers", help="Business identifier.")                
    date_written = fields.Datetime(string="Date Written", help="When prescription was authorized.")                
    patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Patient", help="Who prescription is for.")                
    prescriber_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Prescriber Practitioner", help="Who authorizes the Vision product.")                
    encounter_id = fields.Many2one(comodel_name="hc.res.encounter", string="Encounter", help="Created during encounter / admission / stay.")                
    context_type = fields.Selection(string="Context Type", selection=[("Code", "Code"), ("Condition", "Condition")], help="Type of reason or indication for writing the prescription.")                
    reason_name = fields.Char(string="Reason", compute="_compute_reason_name", store="True", help="Reason or indication for writing the prescription.")                
    reason_code_id = fields.Many2one(comodel_name="hc.vs.vision.prescription.reason", string="Reason Code", help="CodeableConcept reason or indication for writing the prescription.")                
    reason_condition_id = fields.Many2one(comodel_name="hc.res.condition", string="Reason Condition", help="Condition reason or indication for writing the prescription.")                
    dispense_ids = fields.One2many(comodel_name="hc.vision.prescription.dispense", inverse_name="vision_prescription_id", string="Imaging Manifest Studies", help="Vision supply authorization.")                

class VisionPrescriptionDispense(models.Model):    
    _name = "hc.vision.prescription.dispense"    
    _description = "Vision Prescription Dispense"        

    vision_prescription_id = fields.Many2one(comodel_name="hc.res.vision.prescription", string="Vision Prescription", help="Vision prescription associated with this dispense.")                
    product_id = fields.Many2one(comodel_name="hc.vs.vision.product", string="Product", required="True", help="Identifies the type of vision correction product which is required for the patient.")                
    eye = fields.Selection(string="Dispense Eye", selection=[("right", "Right"), ("left", "Left")], help="The eye for which the lens applies.")                
    sphere = fields.Float(string="Sphere", help="Lens power measured in diopters (0.25 units).")                
    cylinder = fields.Float(string="Cylinder", help="Power adjustment for astigmatism measured in diopters (0.25 units).")                
    axis = fields.Integer(string="Axis", help="Adjustment for astigmatism measured in integer degrees.")                
    prism = fields.Float(string="Prism", help="Amount of prism to compensate for eye alignment in fractional units.")                
    base = fields.Selection(string="Dispense Base", selection=[("up", "Up"), ("down", "Down"), ("in", "In"), ("out", "Out")], help="The relative base, or reference lens edge, for the prism.")                
    add = fields.Float(string="Add", help="Power adjustment for multifocal lenses measured in diopters (0.25 units).")                
    power = fields.Float(string="Power", help="Contact lens power measured in diopters (0.25 units).")                
    back_curve = fields.Float(string="Back Curve", help="Back curvature measured in millimeters.")                
    diameter = fields.Float(string="Diameter", help="Contact lens diameter measured in millimeters.")                
    duration = fields.Float(string="Duration", help="The recommended maximum wear period for the lens.")                
    duration_uom_id = fields.Many2one(comodel_name="product.uom", string="Duration UOM", help="Lens wear duration unit of measure.")                
    color = fields.Text(string="Color", help="Special color or pattern.")                
    brand = fields.Text(string="Brand", help="Brand recommendations or restrictions.")                
    notes = fields.Text(string="Notes", help="Notes for special requirements such as coatings and lens materials.")                

class VisionPrescriptionIdentifier(models.Model):    
    _name = "hc.vision.prescription.identifier"    
    _description = "Vision Prescription Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    vision_prescription_id = fields.Many2one(comodel_name="hc.res.vision.prescription", string="Vision Prescription", help="Vision prescription associated with this vision prescription identifier.")                

class VisionPrescriptionReason(models.Model):    
    _name = "hc.vs.vision.prescription.reason"    
    _description = "Vision Prescription Reason"        
    _inherit = ["hc.value.set.contains"]

class VisionProduct(models.Model):    
    _name = "hc.vs.vision.product"    
    _description = "Vision Product"        
    _inherit = ["hc.value.set.contains"]
