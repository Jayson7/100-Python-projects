# pip install  quick-mailer 

from mailer import Mailer 

contact_mail = Mailer(
                 email= 'your email',
                password='your_password',
            )

contact_mail.send( 
                      receiver= 'otudekoferanmi16@gmail.com',
                subject='python mailer test',
                message='Hello, I am the best agent in the world')
print('mail sent')
                