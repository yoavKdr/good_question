using System;

namespace physics_calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            calculator c = new calculator();

            while (true)
            {
                Console.WriteLine("if you want to close the program enter -1");
                Console.WriteLine("Enter how much mass");
                double mass = double.Parse(Console.ReadLine());
                if (mass < 0)
                {
                    break;
                }
                Console.Clear();
                c.Get_info(mass);
            }
        }
    }

    class calculator
    {
        // נתונים דינמיים
        private double m; // המסה של המטען הכבד

        // נתונים סטטיים
        private double team_mass = 35000; // המסע של המטוס עם חברי היחידה וצוות
        private double f = 100000; // כוח המנועים
        private double v = 140; // מהירות המרא

        public calculator()
        {
            m = 0;
        }
        public void Set_m(double m) { this.m = m; } // פונקציה לשינוי המסה של המטען הכבד
        public double Get_m() { return m; } // פונקציה המראה מהוא המסה של המטען הכבד

        public double fly_time()
        {
            return v * (team_mass + m) / f; // t = v/a
        }

        public double mass_to_destroy()
        {
            double max_m = (300000 / 7) - team_mass; // t = v/a => 60 = v/a => 60 = 140m/100000 המסה הגדולה ביותר
            if (m > max_m)
            {
                return m - max_m;
            }
            return 0;
        }

        public double fly_d()
        {
            return v * fly_time() + 0.5 * (f / (team_mass + m)) * Math.Pow(fly_time(), 2);  // x = x0 + vt + 0.5a(t^2)
        }

        public void Get_info(double m)
        {
            Set_m(m);
            Console.WriteLine("the fly destence is {0}", fly_d());
            Console.WriteLine("the fly time is {0}", fly_time());
            Console.WriteLine("if you want to fly in less then 60 sec you need to remove {0} mass \n", mass_to_destroy());
        }
    }
}
