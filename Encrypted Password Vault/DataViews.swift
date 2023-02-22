//
//  DataViews.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/22/23.
//

import SwiftUI

struct DataViews: View {
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

struct DataViews_Previews: PreviewProvider {
    static var previews: some View {
        DataViews(showDataFolderLocation: TestValues.$testFalse, showPasswordCheck: TestValues.$testFalse, showAuthScreen: TestValues.$testTrue)
    }
}
