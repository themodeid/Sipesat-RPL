import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#f0f6fe",
          100: "#dbe8fd",
          200: "#bed7fb",
          500: "#1E6EEB", // Royal Blue from SIPerpus
          600: "#1450B4",
          700: "#0f3d8a",
        },
        navy: {
          800: "#242e42",
          900: "#1C2434", // Deep Navy from SIPerpus
          950: "#141a27",
        },
        surface: {
          light: "#F4F6F9", // Crisp light grey background
          card: "#FFFFFF",
          border: "#E1E6EE",
        },
      },
      fontFamily: {
        sans: ["Segoe UI", "Inter", "system-ui", "-apple-system", "sans-serif"],
      },
    },
  },
  plugins: [],
};
export default config;
