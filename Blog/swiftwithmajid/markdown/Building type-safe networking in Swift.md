##  Building type-safe networking in Swift

10 Feb 2021

More than half of the apps I built during my career had networking code.
Usually, we build apps for web services. Today we will talk about building the
type-safe networking layer using Swift language features like enums, phantom
types, and extensions.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Let’s first take a look at the typical networking code and recognize the
issues that we want to avoid in our solution.

    
    
    struct Repo: Decodable {
        let id: Int
        let name: String
    }
    
    struct SearchResponse: Decodable {
        let items: [Repo]
    }
    
    let query = "Swift"
    let url = URL(string: "https://api.github.com/search/repositories?q=\(query)")!
    var request = URLRequest(url: url)
    request.httpMethod = "GET"
    request.httpBody = nil
    
    let cancellable = URLSession.shared.dataTaskPublisher(for: request)
        .map(\.data)
        .decode(type: SearchResponse.self, decoder: JSONDecoder())
        .map(\.items)
        .replaceError(with: [])
        .sink { print($0) }
    

In the example above, we have a standard networking code that creates the
request and decodes the response. There are a few things that I want to avoid
in the future.

  1. We create a GET request, but there is a possibility to set an HTTP body for a GET request, which looks meaningless. 
  2. We try to decode the response by providing the type of resulting data. Usually, every request has one and only one type that we can obtain. In this case, it is better to have the response type encoded into the request. 

Let’s start building our type-safe networking by introducing the _Request_
type. The _Request_ type should contain the URL we need to access, headers,
and HTTP method.

    
    
    struct Request {
        let url: URL
        let method: HttpMethod
        var headers: [String: String] = [:]
    }
    

The HTTP method is an exclusive thing. You can’t use both GET and POST, and
you can choose only one HTTP method. It looks like a perfect use-case for an
enum type.

    
    
    enum HttpMethod: Equatable {
        case get([URLQueryItem])
        case put(Data?)
        case post(Data?)
        case delete
        case head
    
        var name: String {
            switch self {
            case .get: return "GET"
            case .put: return "PUT"
            case .post: return "POST"
            case .delete: return "DELETE"
            case .head: return "HEAD"
            }
        }
    }
    

As you can see in the example above, we define the _HTTPMethod_ enum that
describes various HTTP methods. We use cases with associated types to hold the
data correlated with the HTTP method. For example, the GET method contains URL
query items, POST and PUT methods have the data we use as the HTTP body.

Now we need to make somehow _URLSession_ working with our _Request_ type. The
easiest way is defining a calculated property on the _Request_ type that
converts it to the _URLRequest_ .

    
    
    extension Request {
        var urlRequest: URLRequest {
            var request = URLRequest(url: url)
    
            switch method {
            case .post(let data), .put(let data):
                request.httpBody = data
            case let .get(queryItems):
                var components = URLComponents(url: url, resolvingAgainstBaseURL: false)
                components?.queryItems = queryItems
                guard let url = components?.url else {
                    preconditionFailure("Couldn't create a url from components...")
                }
                request = URLRequest(url: url)
            default:
                break
            }
    
            request.allHTTPHeaderFields = headers
            request.httpMethod = method.name
            return request
        }
    }
    

Finally, we can create an extension on _URLSession_ to make requests with our
new type.

    
    
    extension URLSession {
        func data(for request: Request) async throws -> Data {
            let (data, _) = try await self.data(for: request.urlRequest)
            return data
        }
    }
    

####  Phantom response type

One thing we forgot to do is encoding of result type into the request. We can
make it really easy by introducing phantom type. Phantom type is a generic
constraint defined in any type but is not used inside. Let’s take a look at
the example.

    
    
    struct Request<Response> {
        let url: URL
        let method: HttpMethod
        var headers: [String: String] = [:]
    }
    

As you can see, we define _Response_ type, but we didn’t use it anywhere in
the _Request_ type. That’s why it is called phantom type. Defining phantom
types allows us to store information about the response in our request type.
For example, it might be a type conforming to _Decodable_ or even an instance
of the _Data_ type. Let’s update our extension on _URLSession_ to support
response decoding.

    
    
    extension URLSession {
        func decode<Value: Decodable>(
            _ request: Request<Value>,
            using decoder: JSONDecoder = .init()
        ) async throws -> Value {
            let (data, _) = try await self.data(for: request.urlRequest)
            return try decoder.decode(Value.self, from: data)
        }
    }
    

In the example above, we introduce the _decode_ function allowing us to fetch
and decode data using our _Request_ type. Take a look at how we use the
phantom type to decode value. Let’s define a Github repo search request using
the new API.

    
    
    extension Request where Response == SearchResponse {
        static func search(matching query: String) -> Self {
            Request(
                url: URL(string: "https://api.github.com/search/repositories")!,
                method: .get(
                    [.init(name: "q", value: query)]
                )
            )
        }
    }
    
    let request: Request<SearchResponse> = .search(matching: "Swift")
    let response = try await URLSession.shared.decode(request)
    

> To learn more about the benefits of using phantom types, look at my [
> “Phantom types in Swift” ](/2021/02/18/phantom-types-in-swift/) post.

####  Conclusion

Today we built a type-safe networking layer using Swift features like enums,
phantom types, and extensions. This toolbox allows you to transform any old
API into a safe and modern API. I hope you enjoy the post. Feel free to follow
me on [ Twitter ](https://twitter.com/mecid) and ask your questions related to
this article. Thanks for reading, and see you next week!
