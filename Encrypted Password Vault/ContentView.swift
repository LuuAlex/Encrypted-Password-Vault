//
//  ContentView.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/12/23.
//

import SwiftUI

struct ContentView: View {
    @State private var path = ""
    @State private var password = ""
    
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!")
            
            TextField("", text: $path) {
                
            }
            .textFieldStyle(RoundedBorderTextFieldStyle())
            TextField("", text: $password) {
                
            }
            .textFieldStyle(RoundedBorderTextFieldStyle())
            Text(String(runRead(path: path, password: password)[0].getPass()))
        }
        .padding()
        
        
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
