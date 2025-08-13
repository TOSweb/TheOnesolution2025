import { Button } from "./ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Input } from "./ui/input";
import { Textarea } from "./ui/textarea";
import { Mail, Phone, MapPin, Clock } from "lucide-react";

export function Contact() {
  return (
    <section id="contact" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl text-gray-900 mb-4">
            Ready to Get Started?
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Let's discuss how we can help transform your digital marketing strategy 
            and drive real results for your business.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <Card>
              <CardHeader>
                <CardTitle>Send us a message</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label htmlFor="name" className="block text-sm mb-2">Name *</label>
                    <Input id="name" placeholder="Your full name" />
                  </div>
                  <div>
                    <label htmlFor="email" className="block text-sm mb-2">Email *</label>
                    <Input id="email" type="email" placeholder="your.email@company.com" />
                  </div>
                </div>
                <div>
                  <label htmlFor="company" className="block text-sm mb-2">Company</label>
                  <Input id="company" placeholder="Your company name" />
                </div>
                <div>
                  <label htmlFor="message" className="block text-sm mb-2">Message *</label>
                  <Textarea 
                    id="message" 
                    placeholder="Tell us about your project and goals..."
                    className="h-32"
                  />
                </div>
                <Button className="w-full sm:w-auto">
                  Send Message
                </Button>
              </CardContent>
            </Card>
          </div>

          <div className="space-y-6">
            <Card>
              <CardContent className="p-6">
                <div className="flex items-center mb-4">
                  <Mail className="h-5 w-5 text-primary mr-3" />
                  <div>
                    <div className="text-gray-900">Email</div>
                    <div className="text-gray-600">hello@digitalpro.com</div>
                  </div>
                </div>
                <div className="flex items-center mb-4">
                  <Phone className="h-5 w-5 text-primary mr-3" />
                  <div>
                    <div className="text-gray-900">Phone</div>
                    <div className="text-gray-600">+1 (555) 123-4567</div>
                  </div>
                </div>
                <div className="flex items-center mb-4">
                  <MapPin className="h-5 w-5 text-primary mr-3" />
                  <div>
                    <div className="text-gray-900">Address</div>
                    <div className="text-gray-600">123 Business Ave<br />Suite 100, City, State 12345</div>
                  </div>
                </div>
                <div className="flex items-center">
                  <Clock className="h-5 w-5 text-primary mr-3" />
                  <div>
                    <div className="text-gray-900">Business Hours</div>
                    <div className="text-gray-600">Mon-Fri: 9AM-6PM<br />Sat-Sun: Closed</div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <div className="bg-primary text-primary-foreground p-6 rounded-lg">
              <h3 className="text-lg mb-3">Free Consultation</h3>
              <p className="text-sm mb-4 opacity-90">
                Get a free 30-minute consultation to discuss your digital marketing goals.
              </p>
              <Button variant="secondary" className="w-full">
                Book Consultation
              </Button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}