//
//  ContentView.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/12/23.
//

import SwiftUI

struct ContentView: View {
    
    @State private var showPathViews = true //!checkPathExists()
    @State private var showPasswordViews = false
    @State private var showDataViews = false
    
    var body: some View {
        VStack {
            if showPathViews {
                PathViews(showPathViews: $showPathViews,
                             showPasswordViews: $showPasswordViews,
                             showDataViews: $showDataViews)
            }
            if showPasswordViews {
                PasswordViews(showPathViews: $showPathViews,
                                 showPasswordViews: $showPasswordViews,
                                 showDataViews: $showDataViews)
            }
            if showDataViews {
                DataViews(showPathViews: $showPathViews,
                         showPasswordViews: $showPasswordViews,
                         showDataViews: $showDataViews)
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
