//
//  ContentView.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/12/23.
//

import SwiftUI

struct ContentView: View {
    @State var showResult: Bool = false
    @State var result: String
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!")
        }
        .padding()
        
        Button(action: {
            result = runPythonCode(read: true)
            showResult.toggle()
        }) {
            Text("See Passwords")
        }
        if showResult {
            Text(String("\(result)"))
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
