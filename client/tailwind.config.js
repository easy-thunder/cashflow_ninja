/** @type {import('tailwindcss')Config} */
// This is the Tailwind CSS configuration file for the client application.
// Usage Example in a React Component:
//
// This example demonstrates how to apply the custom fonts and colors
// defined in the Tailwind configuration to elements in a React component.
//
// To apply a font style, use `font-headline` for headlines and `font-body` for body text.
// Then, apply a font size using `text-h1`, `text-h2`, `text-h3`, `text-h4`, `text-body-lg`, `text-body-md`, or `text-body-sm`.
//
// To apply a color, use the color name such as `text-magnetic-grey`, `text-mint-green`, `text-money-green`, `text-forest-green`, or `text-magnetic-plum`.
// The color names follow the convention `text-{color}` for text colors and `bg-{color}` for background colors.

/*
function Example() {
  return (
    <div>
      <h1 className="font-headline text-h1 text-money-green">Headline 1</h1>
      <h2 className="font-headline text-h2 text-forest-green">Headline 2</h2>
      <h3 className="font-headline text-h3 text-magnetic-plum">Headline 3</h3>
      <h4 className="font-headline text-h4 text-magnetic-grey">Headline 4</h4>
      <p className="font-body text-body-lg text-mint-green">Body Copy 1</p>
      <p className="font-body text-body-md bg-magnetic-grey text-white">Body Copy 2 with background</p>
      <p className="font-body text-body-sm text-magnetic-plum">Body Copy 3</p>
    </div>
  );
}
*/

module.exports = {
    content: [],
    theme: {
        extend: {
            fontFamily: {
                headline: ["Staatliches", "sans-serif"], // Headline font family
                body: ["Rubik", "sans-serif"], // Body text font family
            },
            fontSize: {
                h1: ["3rem", { lineHeight: "1" }], // Headline 1 font size (48px)
                h2: ["2.5rem", { lineHeight: "1" }], // Headline 2 font size (40px)
                h3: ["2rem", { lineHeight: "1" }], // Headline 3 font size (32px)
                h4: ["1.5rem", { lineHeight: "1" }], // Headline 4 font size (24px)
                "body-lg": ["1.5rem", { lineHeight: "1.75" }], // Body large font size (24px)
                "body-md": ["1rem", { lineHeight: "1.5" }], // Body medium font size (16px)
                "body-sm": ["0.75rem", { lineHeight: "1.25" }], // Body small font size (12px)
            },
            colors: {
                // Custom brand colors with examples of usage in comments
                "magnetic-grey": {
                    DEFAULT: "#EAE2F8", // Use for neutral backgrounds or accents
                },
                "mint-green": {
                    DEFAULT: "#99DDCC", // Use for buttons or icons to stand out
                },
                "money-green": {
                    DEFAULT: "#006D33", // Primary brand color for calls to action
                },
                "forest-green": {
                    DEFAULT: "#004D31", // Use for headers or strong emphasis
                },
                "magnetic-plum": {
                    DEFAULT: "#370031", // Use for footer or less prominent elements that require subtlety
                },
            },
        },
    },
    plugins: [],
};
