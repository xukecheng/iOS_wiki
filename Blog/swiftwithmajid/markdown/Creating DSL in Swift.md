##  Creating DSL in Swift

30 Jan 2019

This week we will talk about creating DSL in Swift. Let’s start with the
understanding of DSL acronym. Domain Specific Language is a language hosted by
parent language to solve any specific area. An excellent example of DSL can be
HTML which is DSL for creating web page markup.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

There are some requirements for a language in which you want to create DSL. A
host language should have first-class functions, trailing closures and
operator overloading to make DSL possible. The great news is that Swift has
all of these features.

We are going to simplify User Interface development on iOS by creating UIKit
specific DSL. We have two ways of building UI in iOS. The first one is by
using Interface Builder, and the second one is via code. Both of them have
pros and cons. For instance, building UI by Interface Builder is a high-speed
and visual process, but you have to deal with a problematic code review
process, because of the format of Xibs and Storyboards. In case of building
your UI by code, you get the reusability and clean code review process, but
you deal with the imperative and error-prone codebase, without a visual
understanding of view hierarchy.

Let’s set our goals in building UIKit DSL in Swift:

  1. Visual view hierarchy 
  2. Declarative like HTML 
  3. Type-safe and compile-time guarantee of correctness. 

    
    
    let rootView = stack {
        $0.spacing = 16
        $0.axis = .vertical
        $0.isLayoutMarginsRelativeArrangement = true
    
        $0.stack {
            $0.distribution = .fillEqually
            $0.axis = .horizontal
    
            $0.label {
                $0.textAlignment = .center
                $0.textColor = .white
                $0.text = "Hello"
            }
    
            $0.label {
                $0.textAlignment = .center
                $0.textColor = .white
                $0.text = "World"
            }
    
            $0.customLabel {
                $0.textAlignment = .center
                $0.textColor = .white
                $0.text = "!!!"
            }
        }
    
        let messageButton = $0.button {
            $0.tintColor = .white
            $0.setTitle("Say Hi!", for: .normal)
        }
    
        $0.view {
            $0.backgroundColor = .clear
        }
    }
    

The code above is our target, and this is how we want our DSL to be.
Generally, everything in this example is a function with a trailing closure
parameter. For more details let’s dive into implementation.

####  Root elements

We have to create a function stack which returns _UIStackView_ and accepting
closure which we apply to this new created _UIStackView_ .

    
    
    public func stack(apply closure: (UIStackView) -> Void) -> UIStackView {
        let stack = UIStackView()
        closure(stack)
        return stack
    }
    

These lines give us an opportunity to use stack function similar to HTML tag.

    
    
    stack {
        $0.axis = .vertical
    }
    

As the first parameter of the trailing closure, we get created _UIStackView_
on which we can call customization functions like changing axis, alignment,
etc. Next, we want to call _$0.label_ to configure new _UILabel_ and add to
previous _UIStackView_ . Let’s create an extension for _UIStackView_ which
provides us with label function.

    
    
    extension UIStackView {
        @discardableResult
        public func label(apply closure: (UILabel) -> Void) -> UILabel {
            let label = UILabel()
            addArrangedSubview(label)
            closure(label)
            return label
        }
    }
    

We use _@discardableResult_ annotation to disable swift compiler warning on
ignoring the result of this function because we already added it to
_UIStackView_ . Here is the example of label function usage.

    
    
    stack {
        $0.axis = .vertical
        $0.label {
            $0.adjustsFontForContentSizeCategory = true
        }
    }
    

We have one problem here, and this is the extension on _UIStackView_ , only
_UIStackView_ will have this function. But we need it in any _UIView_
subclass, so let’s move it to _UIView_ extension.

    
    
    extension UIView {
        @discardableResult
        public func label(apply closure: (UILabel) -> Void) -> UILabel {
            let label = UILabel()
            if let stack = self as? UIStackView {
                stack.addArrangedSubview(label)
            } else {
                addSubview(label)
            }
            closure(label)
            return label
        }
    }
    

We try here to cast self to _UIStackView_ , which give us the ability to use
_addArrangedSubview_ in case of _UIStackView_ , if not we add it with the
_addSubview_ method. Next step is populating our _UIView_ extension with
functions for all UIKit components to make above usage possible for every
UIKit component. I’ve added DSL support for all UIKit components. You can
check it out on [ Github ](https://github.com/mecid/UIKitSwiftDSL) .

    
    
    let rootView = stack {
        $0.spacing = 16
        $0.axis = .vertical
        $0.isLayoutMarginsRelativeArrangement = true
    
        $0.stack {
            $0.distribution = .fillEqually
            $0.axis = .horizontal
    
            $0.label {
                $0.textAlignment = .center
                $0.textColor = .white
                $0.text = "Hello"
            }
    
            $0.label {
                $0.textAlignment = .center
                $0.textColor = .white
                $0.text = "World"
            }
    
            $0.customLabel {
                $0.textAlignment = .center
                $0.textColor = .white
                $0.text = "!!!"
            }
        }
    
        let messageButton = $0.button {
            $0.tintColor = .white
            $0.setTitle("Say Hi!", for: .normal)
        }
    
        $0.view {
            $0.backgroundColor = .clear
        }
    }
    

Now we achieve declarative, tree-based and type-safe DSL for building UI for
iOS. [ It is available via CocoaPods and Carthage
](https://github.com/mecid/UIKitSwiftDSL) .

####  Conclusion

Today we learned how powerful is Swift, and how easy we can create DSL for any
specific domain. I suggest you try to develop your DSL for _DispatchQueue_ or
any other area.

Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading and see you next week!

