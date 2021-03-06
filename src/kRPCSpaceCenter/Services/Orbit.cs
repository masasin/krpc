using System;
using KRPC.Service.Attributes;
using KRPCSpaceCenter.ExtensionMethods;
using Tuple3 = KRPC.Utils.Tuple<double,double,double>;

namespace KRPCSpaceCenter.Services
{
    //FIXME: should extend equatable interface?
    [KRPCClass (Service = "SpaceCenter")]
    public sealed class Orbit
    {
        readonly global::Orbit orbit;

        internal Orbit (global::Vessel vessel)
        {
            orbit = vessel.GetOrbit ();
        }

        internal Orbit (global::CelestialBody body)
        {
            if (body == body.referenceBody)
                throw new ArgumentException ("Body does not orbit anything");
            orbit = body.GetOrbit ();
        }

        internal Orbit (global::Orbit orbit)
        {
            this.orbit = orbit;
        }

        //TODO: make equatable? add hashcode???

        [KRPCProperty]
        public CelestialBody Body {
            get { return SpaceCenter.Bodies [orbit.referenceBody.name]; }
        }

        [KRPCProperty]
        public double Apoapsis {
            get { return orbit.ApR; }
        }

        [KRPCProperty]
        public double Periapsis {
            get { return orbit.PeR; }
        }

        [KRPCProperty]
        public double ApoapsisAltitude {
            get { return orbit.ApA; }
        }

        [KRPCProperty]
        public double PeriapsisAltitude {
            get { return orbit.PeA; }
        }

        [KRPCProperty]
        public double SemiMajorAxis {
            get { return 0.5d * (Apoapsis + Periapsis); }
        }

        [KRPCProperty]
        public double SemiMinorAxis {
            get { return SemiMajorAxis * Math.Sqrt (1d - (Eccentricity * Eccentricity)); }
        }

        [KRPCProperty]
        public double Radius {
            get { return orbit.radius; }
        }

        [KRPCProperty]
        public double Speed {
            get { return orbit.orbitalSpeed; }
        }

        [KRPCProperty]
        public double Period {
            get { return orbit.period; }
        }

        [KRPCProperty]
        public double TimeToApoapsis {
            get { return orbit.timeToAp; }
        }

        [KRPCProperty]
        public double TimeToPeriapsis {
            get { return orbit.timeToPe; }
        }

        [KRPCProperty]
        public double Eccentricity {
            get { return orbit.eccentricity; }
        }

        [KRPCProperty]
        public double Inclination {
            get { return orbit.inclination * (Math.PI / 180d); }
        }

        [KRPCProperty]
        public double LongitudeOfAscendingNode {
            get { return orbit.LAN * (Math.PI / 180d); }
        }

        [KRPCProperty]
        public double ArgumentOfPeriapsis {
            get { return orbit.argumentOfPeriapsis * (Math.PI / 180d); }
        }

        [KRPCProperty]
        public double MeanAnomalyAtEpoch {
            get { return orbit.meanAnomalyAtEpoch; }
        }

        [KRPCProperty]
        public double Epoch {
            get { return orbit.epoch; }
        }

        [KRPCProperty]
        public double MeanAnomaly {
            get { return orbit.meanAnomaly; }
        }

        [KRPCProperty]
        public double EccentricAnomaly {
            get { return orbit.eccentricAnomaly; }
        }

        [KRPCMethod]
        public static Tuple3 ReferencePlaneNormal (ReferenceFrame referenceFrame)
        {
            return referenceFrame.DirectionFromWorldSpace (Planetarium.up).normalized.ToTuple ();
        }

        [KRPCMethod]
        public static Tuple3 ReferencePlaneDirection (ReferenceFrame referenceFrame)
        {
            return referenceFrame.DirectionFromWorldSpace (Planetarium.right).normalized.ToTuple ();
        }

        [KRPCProperty]
        public Orbit NextOrbit {
            get {
                return (Double.IsNaN (TimeToSOIChange)) ? null : new Orbit (orbit.nextPatch);
            }
        }

        [KRPCProperty]
        public double TimeToSOIChange {
            get {
                var time = orbit.UTsoi - SpaceCenter.UT;
                return time < 0 ? Double.NaN : time;
            }
        }
    }
}
