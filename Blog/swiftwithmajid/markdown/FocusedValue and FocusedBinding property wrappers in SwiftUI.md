##  FocusedValue and FocusedBinding property wrappers in SwiftUI

03 Mar 2021

The last year Apple has done a great job in terms of focus management in
SwiftUI. We got a few new modifiers to set up an entry point for the focus
system and programmatically handle focus changes. We still have some gaps, and
I hope Apple will fill them during WWDC21. This week I want to talk about
_FocusedValue_ , _FocusedObject_ , and _FocusedBinding_ property wrappers.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  FocusedValue

_FocusedValue_ property wrapper allows us to observe the value from the
focused view or one of its ancestors. It works in a very similar way to the
_Environment_ property wrapper, but instead of observing the environment, it
observes the view hierarchy’s focused view.

> To learn more about the basics of focus management in SwiftUI, take a look
> at my dedicated [ post ](/2020/12/02/focus-management-in-swiftui/) .

To start using this feature, you should first create a struct that conforms to
_FocusedValueKey_ to define the type of value you want to observe. Assume that
we are working on the note-taking app, and we want to monitor the content of
the focused note editor. Let’s try to implement this.

    
    
    struct FocusedNoteValue: FocusedValueKey {
        typealias Value = String
    }
    

As you can see in the example above, we create the _FocusedNoteValue_ struct
and conform to the _FocusedValueKey_ protocol. The only thing we need to do is
adding a type alias for the _Value_ type. The _Value_ type here is our content
that we want to observe when a view is focused. In our case, it is _String_
because we want to monitor the note that the user edits at the moment.

    
    
    extension FocusedValues {
        var noteValue: FocusedNoteValue.Value? {
            get { self[FocusedNoteValue.self] }
            set { self[FocusedNoteValue.self] = newValue }
        }
    }
    

Here we provide an extension for _FocusedValues_ where we register a getter
and setter for our custom focused value. Make sure it is optional. SwiftUI set
it to nil when the view is not focused.

> To learn more about providing custom values via SwiftUI’s Environment, take
> a look at my [ “The power of Environment in SwiftUI” ](/2019/08/21/the-
> power-of-environment-in-swiftui/) post.
    
    
    struct ContentView: View {
        var body: some View {
            Group {
                NoteEditor()
                NotePreview()
            }.border(Color.red)
        }
    }
    
    struct NoteEditor: View {
        @State private var note = "text"
    
        var body: some View {
            TextEditor(text: $note)
                .frame(width: 300, height: 300)
                .focusedValue(\.noteValue, note)
        }
    }
    
    struct NotePreview: View {
        @FocusedValue(\.noteValue) var note
    
        var body: some View {
            Text(note ?? "Note is not focused")
        }
    }
    

Here we have the _ContentView_ with _NoteEditor_ that uses a binding from the
view state to store the note content. We use the _focusedValue_ modifier to
save note content into the special memory that SwiftUI control and only assign
when the view is focused.

We also define the _NotePreview_ view. _NotePreview_ uses the _FocusedValue_
property wrapper to monitor the content of the focused note. SwiftUI will set
the value of _FocusedValue_ to _nil_ as soon as the view loses the focus.

You can use the _focusedSceneValue_ view modifier whenever you need to share
focused value between views in different scenes.

####  FocusedObject

The _FocusedValue_ property wrapper and view modifier works great for value
types. But if you need this behavior for a class conforming to the
_ObservableObject_ protocol you can use the pair of the _focusedObject_ view
modifier and _FocusedObject_ property wrapper.

You can use the _focusedSceneObject_ view modifier whenever you need to share
focused object between views in different scenes.

####  FocusedBinding

OK, we learned how to pass a read-only value for a recently focused note. But
what if we want to modify it? For example, we can have a _NoteFormatter_ view
that formats the note’s content and overrides it. We can’t achieve it with the
_FocusedValue_ property wrapper because it provides us a get-only value.

In this case, we can use the _FocusedBinding_ property wrapper. It works in
the very same way, but instead of the read-only value, it provides a binding
that we can use to override the content. Let’s start by extending the
_FocusedValues_ struct with a custom key for note content binding.

    
    
    struct FocusedNoteBinding: FocusedValueKey {
        typealias Value = Binding<String>
    }
    
    extension FocusedValues {
        var noteBinding: FocusedNoteBinding.Value? {
            get { self[FocusedNoteBinding.self] }
            set { self[FocusedNoteBinding.self] = newValue }
        }
    }
    

Now we can create the _NoteFormatter_ view, which uses the _FocusedBinding_
property wrapper, and override the note content using the binding.

    
    
    struct ContentView: View {
        var body: some View {
            Group {
                NoteEditor()
                NoteFormatter()
            }.border(Color.red)
        }
    }
    
    struct NoteEditor: View {
        @State private var note = "text"
    
        var body: some View {
            TextEditor(text: $note)
                .frame(width: 300, height: 300)
                .focusedValue(\.noteBinding, $note)
        }
    }
    
    struct NoteFormatter: View {
        @FocusedBinding(\.noteBinding) var note
    
        var body: some View {
            VStack {
                Text(note ?? "Note is not focused")
                Button("Clear note") {
                    note = ""
                }
            }
        }
    }
    

####  Conclusion

Today we learned how to use _FocusedValue_ , _FocusedObject_ , and
_FocusedBinding_ property wrappers. One of the possible use cases for these
property wrappers is commands that we can use to create the main menu for
macOS apps. You can access the currently focused view’s content and implement
some logic that lives in your macOS app’s main menu.

> To learn more about building the main menu for macOS apps, take a look at my
> [ “Commands in SwiftUI” ](/2020/11/24/commands-in-swiftui/) post.

I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this article.
Thanks for reading, and see you next week!

