//
//  ContentView.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/12/23.
//

import SwiftUI

struct ContentView: View {
    
    @State private var showDataFolderLocation = true //!checkPathExists()
    @State private var showPasswordCheck = false
    @State private var showAuthScreen = false
    
    var body: some View {
        VStack {
            if showDataFolderLocation {
                FileLocation(showDataFolderLocation: $showDataFolderLocation,
                             showPasswordCheck: $showPasswordCheck,
                             showAuthScreen: $showAuthScreen)
            }
            if showPasswordCheck {
                PasswordLockView(showDataFolderLocation: $showDataFolderLocation,
                                 showPasswordCheck: $showPasswordCheck,
                                 showAuthScreen: $showAuthScreen)
            }
            if showAuthScreen {
                AuthView(showDataFolderLocation: $showDataFolderLocation,
                         showPasswordCheck: $showPasswordCheck,
                         showAuthScreen: $showAuthScreen)
            }
            
            
        }
        .padding()
        
        
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
