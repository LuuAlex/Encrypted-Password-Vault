//
//  ChangeViews.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/17/23.
//

import Foundation
import SwiftUI


struct NextButton: View {
    
    @Binding var showDataFolderLocation: Bool
    @Binding var showPasswordCheck: Bool
    @Binding var showAuthScreen: Bool
    
    @State var path = getPath()
    @State var hide: Bool
    @State var passwordScreen: Bool
    @State var password: String
    
    var body: some View {
        Button ("Next") {
            if passwordScreen {
                if checkHashedPassword(password: password) {
                    showPasswordCheck.toggle()
                    showAuthScreen = true
                } else if !checkPasswordExists() {
                    showPasswordCheck.toggle()
                    showAuthScreen = true
                    setPassword(password: password)
                    runCreateCSV(path: path ?? "~/Downloads", password: password)
                }
            } else {
                showDataFolderLocation.toggle()
                showPasswordCheck = true
            }
        }
        .buttonStyle(.borderedProminent)
        //.foregroundColor(.white)
        .tint(.blue)
        //.cornerRadius(6)
        //.disabled(hide)
    }
    
}


struct FileLocation: View {
    
    @Binding var showDataFolderLocation: Bool
    @Binding var showPasswordCheck: Bool
    @Binding var showAuthScreen: Bool
    
    @State private var placeholder = "Select Folder"
    @State private var filename = ""

    var body: some View {
        VStack {
            
            HStack {
                let _ = print(initalize())
                Text("Password Data Folder Location: ")
                Button(placeholder) {
                    let panel = NSOpenPanel()
                    panel.allowsMultipleSelection = false
                    panel.canChooseDirectories = true
                    panel.canChooseFiles = false
                    if panel.runModal() == .OK {
                        self.placeholder = panel.url?.lastPathComponent ?? "Select Folder"
                        self.filename = panel.url?.path ?? ""
                        setPath(path: self.filename) // TODO
                        panel.close()
                    }
                }
            }

            NextButton(showDataFolderLocation: $showDataFolderLocation,
                       showPasswordCheck: $showPasswordCheck,
                       showAuthScreen: $showAuthScreen,
                       hide: filename.isEmpty,
                       passwordScreen: false,
                       password: "")
                
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
    
}


struct PasswordLockView: View {
    
    @Binding var showDataFolderLocation: Bool
    @Binding var showPasswordCheck: Bool
    @Binding var showAuthScreen: Bool
    
    @State private var password = ""
    
    var body: some View {
        VStack {
            HStack {
                Text("Enter your password: ")
                TextField("", text: $password)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
            }
            
            NextButton(showDataFolderLocation: $showDataFolderLocation,
                       showPasswordCheck: $showPasswordCheck,
                       showAuthScreen: $showAuthScreen,
                       hide: password.isEmpty,
                       passwordScreen: true,
                       password: password)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
    
}


struct AuthView: View {
    
    @Binding var showDataFolderLocation: Bool
    @Binding var showPasswordCheck: Bool
    @Binding var showAuthScreen: Bool
    
    @State var password = getPassword()
    @State var path = getPath()
    
    var body: some View {
        VStack {
            var data = runRead(path: path ?? "~/Downloads", password: password ?? "")
            Grid() {
                ForEach((0...data.count), id: \.self) { i in
                    GridRow {
                        Text(data[i].getKey())
                        Text(data[i].getUser())
                        Text(data[i].getPass())
                    }
                }
            }
            
            NextButton(showDataFolderLocation: $showDataFolderLocation,
                       showPasswordCheck: $showPasswordCheck,
                       showAuthScreen: $showAuthScreen,
                       hide: false,
                       passwordScreen: false,
                       password: password ?? "")
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
    
}
