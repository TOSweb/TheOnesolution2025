import { Button } from "./ui/button";
import { Menu, X } from "lucide-react";
import { useState } from "react";

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <span className="text-2xl text-primary tracking-tight">DigitalPro</span>
            </div>
          </div>
          
          <nav className="hidden md:block">
            <div className="ml-10 flex items-baseline space-x-8">
              <a href="#services" className="text-gray-600 hover:text-primary px-3 py-2 transition-colors">
                Services
              </a>
              <a href="#about" className="text-gray-600 hover:text-primary px-3 py-2 transition-colors">
                About
              </a>
              <a href="#testimonials" className="text-gray-600 hover:text-primary px-3 py-2 transition-colors">
                Testimonials
              </a>
              <a href="#contact" className="text-gray-600 hover:text-primary px-3 py-2 transition-colors">
                Contact
              </a>
            </div>
          </nav>

          <div className="hidden md:block">
            <Button>Get Started</Button>
          </div>

          <div className="md:hidden">
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-600 hover:text-primary hover:bg-gray-100"
            >
              {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </button>
          </div>
        </div>

        {isMenuOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-white border-t">
              <a href="#services" className="block px-3 py-2 text-gray-600 hover:text-primary">
                Services
              </a>
              <a href="#about" className="block px-3 py-2 text-gray-600 hover:text-primary">
                About
              </a>
              <a href="#testimonials" className="block px-3 py-2 text-gray-600 hover:text-primary">
                Testimonials
              </a>
              <a href="#contact" className="block px-3 py-2 text-gray-600 hover:text-primary">
                Contact
              </a>
              <div className="px-3 py-2">
                <Button className="w-full">Get Started</Button>
              </div>
            </div>
          </div>
        )}
      </div>
    </header>
  );
}