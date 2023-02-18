//
//  ContentView.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/12/23.
//

import SwiftUI

struct ContentView: View {
    @State private var path = "/Users/alexluu/Downloads"
    @State private var password = "123"
    
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!")
            
            TextField("/Users/alexluu/Downloads", text: $path)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            TextField("123", text: $password)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            let _ = print(runCreateCSV(path: path, password: password))
            let _ = print(runWrite(path: path, password: password, newDataEntry: ["ufe","xsf","12"]))
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
