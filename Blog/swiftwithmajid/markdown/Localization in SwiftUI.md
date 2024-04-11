##  Localization in SwiftUI

16 Oct 2019

This week I want to talk about another crucial feature of any app, which is
_Localization_ . Every user expects that your app correctly uses environment
features like the right-to-left layout or uses system locale to format dates
or currencies. Another vital thing here is translations, and this week, we
will learn which tools SwiftUI provides to add in our apps as many languages
as we can.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  LocalizedStringKey

_LocalizedStringKey_ is a special struct which is provided by the SwiftUI
framework. It conforms _ExpressibleByStringLiteral_ protocol, which allows us
to create this struct by using a _String_ value. _Text_ component, on the
other hand, has an overload that accepts _LocalizedStringKey_ instead of
_String_ . It allows us to use our localization keys in a very transparent
way. Let’s take a look at a quick example.

    
    
    let goal: LocalizedStringKey = "goal"
    let text = Text(goal)
    

_LocalizedStringKey_ looks for a _“goal”_ key in translation files, and as
soon as it finds provided translation for a key _“goal”_ it will replace the
key with a correct translated string. In the case where there is no provided
translation, it will use the key as a dummy string value.

To learn how to create translation files, take a look at the [
“Internationalization and Localization”
](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LocalizingYourApp/LocalizingYourApp.html#//apple_ref/doc/uid/10000171i-CH5-SW1)
guide provided by Apple.

####  String interpolation

We already know how to localize static text in our apps. But what about the
dynamic text, where we need to inject some data like names or some numeric
values. Fortunately, _LocalizedStringKey_ conforms
_ExpressibleByStringInterpolation_ protocol, which allows us to use _String_
interpolation to pass data into our string values. Let’s take a look at a
small example.

    
    
    let name = "Majid"
    Text("myNameIs \(name)")
    

In the example above, we create a _Text_ component with the _“myNameIs
(name)”_ string value. As you already know, the Text component has an init
method overload, which accepts _LocalizedStringKey_ and _LocalizedStringKey_
conforms _ExpressibleByStringInterpolation_ , and **this is all the magic
behind the localization in SwiftUI** . This piece of code will look for the
_“myNameIs %@”_ key in your translation files. Let’s take a look at how our
translation file should look to make it work.

    
    
    "myNameIs %@" = "My name is %@.";
    

**I have to mention that it doesn’t work in preview canvas. You should run it
on simulator.**

_String_ interpolation is a compelling feature of Swift language. By using
_String_ interpolation, we can also pass stuff like formatters or format
specifiers, which can provide additional presentation logic. Let’s take a look
at a few code examples.

    
    
    let date = Date()
    let formatter = DateFormatter()
    formatter.dateStyle = .medium
    formatter.timeStyle = .none
    Text("birthday \(date, formatter: formatter)")
    

In the code sample above, we pass a _DateFormatter_ , which converts a _Date_
representation into a proper localized string value. This code will run a
localized string lookup and then apply the formatter. Here is how the
translation file should look.

    
    
    "birthday %@" = "My birthday is %@.";
    

Let’s take a look at another quick sample where we inject integer into our
translation.

    
    
    let age = 28
    Text("age \(age)")
    
    "age %lld" = "I'm %lld years old";
    

####  Conclusion

Localization is an essential aspect in the world of user experience. Today we
learned how easily we could localize our apps with the help of
_LocalizedStringKey_ struct provided by SwiftUI. I hope you enjoy the post.
Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading, and see you next week!

