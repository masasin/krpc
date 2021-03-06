import unittest
import testingtools
import krpc
from mathtools import dot

class TestPartsPart(testingtools.TestCase):

    @classmethod
    def setUpClass(cls):
        if krpc.connect().space_center.active_vessel.name != 'Parts':
            testingtools.new_save()
            testingtools.launch_vessel_from_vab('Parts')
            testingtools.remove_other_vessels()
        cls.conn = krpc.connect(name='TestParts')
        cls.vessel = cls.conn.space_center.active_vessel
        cls.parts = cls.vessel.parts

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def test_root_part(self):
        part = self.parts.root
        self.assertEqual('Mark1-2Pod', part.name)
        self.assertEqual('Mk1-2 Command Pod', part.title)
        self.assertEqual(3800, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual(None, part.parent)
        self.assertEqual(
            ['LT-1 Landing Struts', 'LT-1 Landing Struts', 'LT-1 Landing Struts',
             'Mk16-XL Parachute', 'Reflectron DP-10', 'Small Gear Bay', 'TR-XL Stack Separator'],
            sorted(p.title for p in part.children))
        self.assertTrue(part.axially_attached)
        self.assertFalse(part.radially_attached)
        self.assertEquals(-1, part.stage)
        self.assertEquals(-1, part.decouple_stage)
        self.assertFalse(part.massless)
        self.assertClose(4120, part.mass)
        self.assertClose(4000, part.dry_mass)
        self.assertEqual(45, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(3400, part.max_temperature, 0.5)
        self.assertTrue(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        modules = ['FlagDecal', 'ModuleCommand', 'ModuleReactionWheel',
                   'ModuleScienceContainer', 'ModuleScienceExperiment', 'ModuleTripLogger']
        if self.conn.space_center.far_available:
            modules.extend(['FARBasicDragModel', 'FARControlSys'])
        self.assertEqual(sorted(modules), sorted(m.name for m in part.modules))
        self.assertEqual(None, part.decoupler)
        self.assertEqual(None, part.docking_port)
        self.assertEqual(None, part.engine)
        self.assertEqual(None, part.landing_leg)
        self.assertEqual(None, part.launch_clamp)
        self.assertEqual(None, part.light)
        self.assertEqual(None, part.parachute)
        self.assertNotEqual(None, part.reaction_wheel)
        self.assertEqual(None, part.sensor)
        self.assertEqual(None, part.solar_panel)

    def test_control_from(self):
        ref = self.vessel.orbit.body.reference_frame
        root = self.parts.root
        port = self.parts.with_title('Clamp-O-Tron Docking Port')[0]

        # Check vessel direction is in direction of root part
        # and perpendicular to the docking port
        vessel_dir = self.vessel.direction(ref)
        root_dir = root.direction(ref)
        port_dir = port.direction(ref)
        self.assertClose(vessel_dir, root_dir)
        self.assertClose(0, dot(vessel_dir, port_dir))

        # Control from the docking port
        port.control_from()

        # Check vessel direction is now the direction of the docking port
        vessel_dir = self.vessel.direction(ref)
        self.assertClose(0, dot(vessel_dir, root_dir))
        self.assertClose(vessel_dir, port_dir)

        # Control from the root part
        root.control_from()

        # Check vessel direction is now the direction of the root part
        vessel_dir = self.vessel.direction(ref)
        self.assertClose(vessel_dir, root_dir)
        self.assertClose(0, dot(vessel_dir, port_dir))

    def test_decoupler(self):
        part = self.parts.with_title('TT-70 Radial Decoupler')[0]
        self.assertEqual('radialDecoupler2', part.name)
        self.assertEqual('TT-70 Radial Decoupler', part.title)
        self.assertEqual(700, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual('Rockomax Jumbo-64 Fuel Tank', part.parent.title)
        self.assertEqual(['S1 SRB-KD25k'], [p.title for p in part.children])
        self.assertFalse(part.axially_attached)
        self.assertTrue(part.radially_attached)
        self.assertEquals(5, part.stage)
        self.assertEquals(5, part.decouple_stage)
        self.assertFalse(part.massless)
        self.assertClose(50, part.mass)
        self.assertClose(50, part.dry_mass)
        self.assertEqual(8, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(3200, part.max_temperature, 0.5)
        self.assertTrue(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        modules = ['ModuleAnchoredDecoupler', 'ModuleTestSubject']
        if self.conn.space_center.far_available:
            modules.append('FARBasicDragModel')
        self.assertEqual(sorted(modules), sorted(m.name for m in part.modules))
        self.assertNotEqual(None, part.decoupler)
        self.assertEqual(None, part.reaction_wheel)

    def test_docking_port(self):
        part = self.parts.with_title('Clamp-O-Tron Docking Port')[0]
        self.assertEqual('dockingPort2', part.name)
        self.assertEqual('Clamp-O-Tron Docking Port', part.title)
        self.assertEqual(280, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual('Rockomax X200-32 Fuel Tank', part.parent.title)
        self.assertEqual([], [p.title for p in part.children])
        self.assertFalse(part.axially_attached)
        self.assertTrue(part.radially_attached)
        self.assertEquals(-1, part.stage)
        self.assertEquals(3, part.decouple_stage)
        self.assertFalse(part.massless)
        self.assertClose(50, part.mass)
        self.assertClose(50, part.dry_mass)
        self.assertEqual(10, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(3400, part.max_temperature, 0.5)
        self.assertTrue(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        modules = ['ModuleDockingNode', 'ModuleDockingNodeNamed']
        if self.conn.space_center.far_available:
            modules.append('FARBasicDragModel')
        self.assertEqual(sorted(modules), sorted(m.name for m in part.modules))
        self.assertNotEqual(None, part.docking_port)

    def test_engine(self):
        part = self.parts.with_title('S1 SRB-KD25k')[0]
        self.assertEqual('MassiveBooster', part.name)
        self.assertEqual('S1 SRB-KD25k', part.title)
        self.assertEqual(1800, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual('TT-70 Radial Decoupler', part.parent.title)
        self.assertEqual(['Aerodynamic Nose Cone'], [p.title for p in part.children])
        self.assertFalse(part.axially_attached)
        self.assertTrue(part.radially_attached)
        self.assertEquals(6, part.stage)
        self.assertEquals(5, part.decouple_stage)
        self.assertFalse(part.massless)
        self.assertClose(21750, part.mass)
        self.assertClose(3000, part.dry_mass)
        self.assertEqual(7, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(3900, part.max_temperature, 0.5)
        self.assertTrue(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        modules = ['FlagDecal', 'ModuleAnimateHeat', 'ModuleEnginesFX', 'ModuleTestSubject']
        if self.conn.space_center.far_available:
            modules.append('FARBasicDragModel')
        self.assertEqual(sorted(modules), sorted(m.name for m in part.modules))
        self.assertNotEqual(None, part.engine)

    def test_landing_leg(self):
        part = self.parts.with_title('LT-1 Landing Struts')[0]
        self.assertEqual('landingLeg1', part.name)
        self.assertEqual('LT-1 Landing Struts', part.title)
        self.assertEqual(240, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual('Mk1-2 Command Pod', part.parent.title)
        self.assertEqual([], [p.title for p in part.children])
        self.assertFalse(part.axially_attached)
        self.assertTrue(part.radially_attached)
        self.assertEquals(-1, part.stage)
        self.assertEquals(-1, part.decouple_stage)
        self.assertFalse(part.massless)
        self.assertClose(50, part.mass)
        self.assertClose(50, part.dry_mass)
        self.assertEqual(12, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(2900, part.max_temperature, 0.5)
        self.assertTrue(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        modules = ['ModuleLandingLeg']
        if self.conn.space_center.far_available:
            modules.append('FARBasicDragModel')
        self.assertEqual(sorted(modules), sorted(m.name for m in part.modules))
        self.assertNotEqual(None, part.landing_leg)

    def test_launch_clamp(self):
        part = self.parts.with_title('TT18-A Launch Stability Enhancer')[0]
        self.assertEqual('launchClamp1', part.name)
        self.assertEqual('TT18-A Launch Stability Enhancer', part.title)
        self.assertEqual(200, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual('Rockomax Jumbo-64 Fuel Tank', part.parent.title)
        self.assertEqual(len(part.children), 0)
        self.assertFalse(part.axially_attached)
        self.assertTrue(part.radially_attached)
        self.assertEquals(6, part.stage)
        self.assertEquals(6, part.decouple_stage)
        self.assertFalse(part.massless)
        self.assertClose(100, part.mass)
        self.assertClose(100, part.dry_mass)
        self.assertEqual(100, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(5000, part.max_temperature, 0.5)
        self.assertFalse(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        modules = ['LaunchClamp', 'ModuleGenerator', 'ModuleTestSubject']
        if self.conn.space_center.remote_tech_available:
            modules.append('ModuleRTAntennaPassive')
        self.assertEqual(sorted(modules), sorted(m.name for m in part.modules))
        self.assertNotEqual(None, part.launch_clamp)

    def test_light(self):
        part = self.parts.with_title('Illuminator Mk1')[0]
        self.assertEqual('spotLight1', part.name)
        self.assertEqual('Illuminator Mk1', part.title)
        self.assertEqual(100, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual('Aerodynamic Nose Cone', part.parent.title)
        self.assertEqual(0, len(part.children))
        self.assertFalse(part.axially_attached)
        self.assertTrue(part.radially_attached)
        self.assertEquals(-1, part.stage)
        self.assertEquals(5, part.decouple_stage)
        self.assertTrue(part.massless)
        self.assertClose(0, part.mass)
        self.assertClose(0, part.dry_mass)
        self.assertEqual(8, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(3200, part.max_temperature, 0.5)
        self.assertTrue(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        modules = ['ModuleLight']
        if self.conn.space_center.far_available:
            modules.append('FARBasicDragModel')
        self.assertEqual(sorted(modules), sorted(m.name for m in part.modules))
        self.assertNotEqual(None, part.light)

    def test_parachute(self):
        part = self.parts.with_title('Mk16-XL Parachute')[0]
        self.assertEqual('parachuteLarge', part.name)
        self.assertEqual('Mk16-XL Parachute', part.title)
        self.assertEqual(850, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual('Mk1-2 Command Pod', part.parent.title)
        self.assertEqual(0, len(part.children))
        self.assertTrue(part.axially_attached)
        self.assertFalse(part.radially_attached)
        self.assertEquals(0, part.stage)
        self.assertEquals(-1, part.decouple_stage)
        self.assertFalse(part.massless)
        self.assertClose(300, part.mass)
        self.assertClose(300, part.dry_mass)
        self.assertEqual(12, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(3100, part.max_temperature, 0.5)
        self.assertTrue(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        self.assertEqual(['ModuleParachute', 'ModuleTestSubject'], sorted(m.name for m in part.modules))
        self.assertNotEqual(None, part.parachute)

    def test_sensor(self):
        part = self.parts.with_title('PresMat Barometer')[0]
        self.assertEqual('sensorBarometer', part.name)
        self.assertEqual('PresMat Barometer', part.title)
        self.assertEqual(3300, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual('Rockomax X200-8 Fuel Tank', part.parent.title)
        self.assertEqual(0, len(part.children))
        self.assertFalse(part.axially_attached)
        self.assertTrue(part.radially_attached)
        self.assertEquals(-1, part.stage)
        self.assertEquals(1, part.decouple_stage)
        self.assertTrue(part.massless)
        self.assertClose(0, part.mass)
        self.assertClose(0, part.dry_mass)
        self.assertEqual(8, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(3200, part.max_temperature, 0.5)
        self.assertTrue(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        modules = ['ModuleEnviroSensor', 'ModuleScienceExperiment']
        if self.conn.space_center.far_available:
            modules.append('FARBasicDragModel')
        self.assertEqual(sorted(modules), sorted(m.name for m in part.modules))
        self.assertNotEqual(None, part.sensor)

    def test_solar_panel(self):
        part = self.parts.with_title('Gigantor XL Solar Array')[0]
        self.assertEqual('largeSolarPanel', part.name)
        self.assertEqual('Gigantor XL Solar Array', part.title)
        self.assertEqual(3000, part.cost)
        self.assertEqual(self.vessel, part.vessel)
        self.assertEqual('FL-R1 RCS Fuel Tank', part.parent.title)
        self.assertEqual(0, len(part.children))
        self.assertFalse(part.axially_attached)
        self.assertTrue(part.radially_attached)
        self.assertEquals(-1, part.stage)
        self.assertEquals(3, part.decouple_stage)
        self.assertFalse(part.massless)
        self.assertClose(350, part.mass)
        self.assertClose(350, part.dry_mass)
        self.assertEqual(8, part.impact_tolerance)
        self.assertGreater(part.temperature, 15)
        self.assertLess(part.temperature, 25)
        self.assertClose(3200, part.max_temperature, 0.5)
        self.assertTrue(part.crossfeed)
        self.assertEquals(0, len(part.fuel_lines_from))
        self.assertEquals(0, len(part.fuel_lines_to))
        modules = ['ModuleDeployableSolarPanel']
        if self.conn.space_center.far_available:
            modules.append('FARBasicDragModel')
        self.assertEqual(sorted(modules), sorted(m.name for m in part.modules))
        self.assertNotEqual(None, part.solar_panel)

if __name__ == "__main__":
    unittest.main()
